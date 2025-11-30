from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
import tensorflow as tf
import pickle
import re
import nltk
from nltk.corpus import stopwords
from database import SessionLocal, User, Review, hash_password

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class SignUpRequest(BaseModel):
    email: EmailStr
    password: str

class ReviewRequest(BaseModel):
    email: EmailStr
    text: str

class ReviewResponse(BaseModel):
    sentiment: str
    confidence: float
    message: str

class AuthResponse(BaseModel):
    success: bool
    message: str
    email: str = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ReviewPredictor:
    def __init__(self, model_path='saved_model'):
        self.model = tf.keras.models.load_model(f'{model_path}/hotel_review_model.h5')
        with open(f'{model_path}/tokenizer.pkl', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        with open(f'{model_path}/max_seq_length.pkl', 'rb') as handle:
            self.max_seq_length = pickle.load(handle)
        negations = {"no", "not", "never", "n't"}
        stopset = set(stopwords.words("english")) - negations
        self.stopwords = stopset

    def process_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s']", " ", text)
        text = re.sub(r'\d+', ' ', text)
        words = text.split()
        words = [w for w in words if w not in self.stopwords]
        return ' '.join(words)

    def predict_sentiment(self, text):
        processed = self.process_text(text)
        seq = self.tokenizer.texts_to_sequences([processed])
        padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=self.max_seq_length, padding='post')
        pred = float(self.model.predict(padded, verbose=0)[0][0])
        negative_prob = pred
        positive_prob = 1.0 - pred
        if positive_prob >= negative_prob:
            return "POSITIVE", positive_prob
        else:
            return "NEGATIVE", negative_prob

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = ReviewPredictor()

@app.get("/")
async def root():
    return {"status": "ready"}

@app.post("/signup", response_model=AuthResponse)
@app.post("/signup/")
async def signup(request: SignUpRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = hash_password(request.password)
    new_user = User(email=request.email, password=hashed_pw)
    db.add(new_user)
    db.commit()
    return AuthResponse(success=True, message="Account created successfully!", email=request.email)

@app.post("/login", response_model=AuthResponse)
@app.post("/login/")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Account not found. Please sign up.")
    hashed_pw = hash_password(request.password)
    if user.password != hashed_pw:
        raise HTTPException(status_code=401, detail="Incorrect password")
    return AuthResponse(success=True, message="Login successful!", email=user.email)

@app.post("/analyze", response_model=ReviewResponse)
@app.post("/analyze/")
async def analyze_review(request: ReviewRequest, db: Session = Depends(get_db)):
    sentiment, confidence = predictor.predict_sentiment(request.text)
    new_review = Review(
        user_email=request.email,
        review_text=request.text,
        sentiment=sentiment,
        confidence=confidence
    )
    db.add(new_review)
    db.commit()
    return ReviewResponse(
        sentiment=sentiment,
        confidence=confidence,
        message=f"Review analyzed! Sentiment: {sentiment} (Confidence: {(confidence*100):.2f}%)"
    )
