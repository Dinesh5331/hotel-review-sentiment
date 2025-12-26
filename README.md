# Resenas - Hotel Review Sentiment Analysis

AI-powered hotel review sentiment analyzer with user authentication.



### 1. Backend Setup
```bash
# Navigate to backend folder
cd "GEN AI project/ml model"

# Create virtual environment
python -m venv myenv

# Activate virtual environment
myenv\Scripts\activate          # Windows
source myenv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Train the model (first time only - takes 10-20 mins)
python model.py

# Start backend server
uvicorn predict_review:app --reload --host 0.0.0.0 --port 8000
```

Backend runs at: `http://localhost:8000`

### 2. Frontend Setup (New Terminal)
```bash
# Navigate to frontend folder
cd "GEN AI project/my-react-app"

# Install dependencies
npm install

# Start frontend
npm run dev
```

Frontend runs at: `http://localhost:5173`

## 📖 Usage

1. Open `http://localhost:5173` in your browser
2. Click **"Create now"** to sign up
3. Enter email and password → Click **"Sign up"**
4. Write a hotel review → Click **"Submit Review"**
5. View sentiment analysis result (POSITIVE/NEGATIVE)


## 📁 Project Structure
```
GEN-AI-project/
│
├── ml-model/
│   ├── model.py              # Train model
│   ├── predict_review.py     # Backend API
│   ├── database.py           # Database setup
│   ├── requirements.txt      # Python packages
│   ├── saved_model/          # Trained model files
│   └── users.db              # SQLite database (auto-generated)
│
└── my-react-app/
    ├── src/
    │   ├── LoginPage.jsx     # Login page
    │   ├── SignUp.jsx        # Sign up page
    │   ├── HotelReview.jsx   # Review page
    │   └── main.jsx          # App entry point
    ├── package.json          # Node packages
    └── vite.config.js        # Vite config
```
**⚠️ Both servers must be running simultaneously for the app to work!**