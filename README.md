HOTEL REVIEW SENTIMENT ANALYSIS

A full-stack AI-powered web application that analyzes hotel reviews to determine sentiment (Positive/Negative) using machine learning.


FEATURES


USER AUTHENTICATION

    Secure Signup with email and password

    Password Hashing using SHA-256

    Protected Login system

    Inline UI Messages - clean error/success notifications without pop-ups

AI SENTIMENT ANALYSIS

    TensorFlow GRU Model for accurate predictions

    Custom Text Preprocessing with tokenization and sequence padding

    Confidence Scoring for each prediction

    Real-time Analysis with instant results

DATABASE MANAGEMENT

    SQLite Database with SQLAlchemy ORM

    User Management - store user accounts securely

    Review History - save all analyzed reviews

    Prediction Storage - maintain historical data

MODERN USER INTERFACE

    React + Vite frontend for fast performance

    Responsive Design works on all devices

    Clean Interface with professional styling

    Intuitive Navigation between pages


BACKEND SETUP (FASTAPI + TENSORFLOW)

    Navigate to the backend folder
    cd "GEN AI project/ml model"

    Create a virtual environment
    python -m venv myenv

    Activate the environment
    Windows: myenv\Scripts\activate
    Mac/Linux: source myenv/bin/activate

    Install dependencies
    pip install -r requirements.txt

    Start the FastAPI server
    uvicorn predict_review:app --reload --host 0.0.0.0 --port 8000

Backend will run on: http://localhost:8000
API Documentation: http://localhost:8000/docs

FRONTEND SETUP (REACT + VITE)

    Open a new terminal

    Navigate to the frontend folder
    cd "GEN AI project/my-react-app"

    Install dependencies
    npm install

    Start the development server
    npm run dev

Frontend will run on: http://localhost:5173

========================================================================
MACHINE LEARNING MODEL
========================================================================

The sentiment analysis is powered by a sophisticated neural network:

    Architecture: GRU-based neural network

    Vocabulary: Tokenizer with top 10,000 words

    Preprocessing: Custom stopword filtering and text cleaning

    Sequence Handling: Padding to max sequence length

    Classification: Binary classification (Positive/Negative)

Model Files:

    hotel_review_model.h5 - Trained TensorFlow model

    tokenizer.pkl - Text tokenizer for preprocessing

    max_seq_length.pkl - Sequence length configuration

========================================================================
API ENDPOINTS
========================================================================

AUTHENTICATION ENDPOINTS

    POST /signup - Create a new user account

    POST /login - Authenticate user and generate session

ANALYSIS ENDPOINTS

    POST /analyze - Submit review text and receive sentiment analysis

========================================================================
DATABASE SCHEMA
========================================================================

USERS TABLE
Column	Type	Description
id	Integer	Primary key
email	String	User's email (unique)
password	String	Hashed password
created_at	DateTime	Account creation timestamp

REVIEWS TABLE
Column	Type	Description
id	Integer	Primary key
user_email	String	Associated user's email
review_text	String	Original review text
sentiment	String	Prediction result (Positive/Negative)
confidence	Float	Model confidence score (0-1)
created_at	DateTime	Analysis timestamp

========================================================================
QUICK START
========================================================================

RUNNING THE FULL PROJECT

    Start the Backend:
    cd "ml model"
    myenv\Scripts\activate # Windows
    source myenv/bin/activate # Mac/Linux

    pip install -r requirements.txt
    uvicorn predict_review:app --reload --port 8000

    Start the Frontend:
    cd "my-react-app"
    npm install
    npm run dev

    Open your browser: http://localhost:5173

========================================================================
USAGE GUIDE
========================================================================

    Create an Account - Sign up with your email and password

    Login - Access your account securely

    Submit Reviews - Enter hotel reviews in the text area

    Get Analysis - Receive instant sentiment predictions with confidence scores

    View History - All your analyses are stored for future reference

========================================================================
TECHNOLOGY STACK
========================================================================

    Frontend: React, Vite, Modern CSS

    Backend: FastAPI, Python

    Machine Learning: TensorFlow, Keras, GRU Neural Networks

    Database: SQLite with SQLAlchemy ORM

    Authentication: SHA-256 Password Hashing

========================================================================
LICENSE
========================================================================

MIT License - feel free to use this project for personal or commercial purposes.
