Hotel Review Sentiment Analysis (React + FastAPI + TensorFlow)

This project is a full-stack AI-powered sentiment analysis platform that allows users to:

Create an account

Log in securely

Submit hotel reviews

Get instant Positive / Negative sentiment predictions

View prediction confidence

Store user reviews in a SQLite database

Interact through a clean React frontend

Use a FastAPI + TensorFlow backend

⭐ Features
🔐 User Authentication

Signup with email + password

Password hashing (SHA-256)

Secure login

Inline UI error & success messages (no pop-up alerts)

🤖 AI Sentiment Analysis

TensorFlow GRU model

Tokenization + sequence padding

Custom text preprocessing

Confidence score for each review

🗄 Database (SQLite + SQLAlchemy)

Saves users

Saves reviews

Stores predictions for future usage

🎨 Modern UI (React + Vite)

Signup page

Login page

Review submission page

Result display with confidence

Smooth, professional interface

📂 Project Structure
GEN AI project/
│
├── README.md                     # Documentation for the project
│
├── my-react-app/                 # Frontend (React + Vite)
│   ├── src/
│   │   ├── LoginPage.jsx
│   │   ├── SignUp.jsx
│   │   ├── HotelReview.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── ...
│
└── ml model/                     # Backend (FastAPI + TensorFlow + SQLite)
    ├── predict_review.py         # API server
    ├── database.py               # SQLAlchemy models & DB setup
    ├── model.py                  # ML training script
    ├── saved_model/              # Saved TensorFlow model + tokenizer
    ├── users.db                  # SQLite database (auto-generated)
    └── requirements.txt          # Backend Python dependencies

⚙️ Backend Setup (FastAPI + TensorFlow)
1️⃣ Navigate to the backend folder
cd "GEN AI project/ml model"

2️⃣ Create a virtual environment
python -m venv myenv

3️⃣ Activate the environment

Windows:

myenv\Scripts\activate


Mac/Linux:

source myenv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Start the FastAPI server
uvicorn predict_review:app --reload --host 0.0.0.0 --port 8000

Backend will run on:

http://localhost:8000

API Docs: http://localhost:8000/docs

🎨 Frontend Setup (React + Vite)
1️⃣ Open a new terminal
2️⃣ Navigate to the frontend folder
cd "GEN AI project/my-react-app"

3️⃣ Install node modules
npm install

4️⃣ Start React development server
npm run dev

Frontend will run on:

http://localhost:5173

🤖 Machine Learning Model

The ML model was trained using:

TensorFlow

GRU-based neural network

Tokenizer with top 10,000 words

Padding to max sequence length

Custom stopword filtering

Binary classification (Positive / Negative)

Model files saved in:

ml model/saved_model/


Files include:

hotel_review_model.h5

tokenizer.pkl

max_seq_length.pkl

🌐 API Endpoints
➤ POST /signup

Create a new user

➤ POST /login

Verify email + password

➤ POST /analyze

Submit review → receive sentiment + confidence

🗄 Database Structure
users table
Column	Type
id	Integer
email	String
password	String
created_at	DateTime
reviews table
Column	Type
id	Integer
user_email	String
review_text	String
sentiment	String
confidence	Float
created_at	DateTime
🚀 How to Run Full Project (Summary)
Backend:
cd ml model
myenv\Scripts\activate
pip install -r requirements.txt
uvicorn predict_review:app --reload --port 8000

Frontend:
cd my-react-app
npm install
npm run dev


Then open:
👉 http://localhost:5173

📝 License

MIT License — free to use.