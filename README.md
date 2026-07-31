# 🎓 Student Marks Predictor

A machine learning web app that predicts a student's expected marks based on their daily study hours, built with a Linear Regression model and deployed using Streamlit.

## 🔗 Live Demo
https://bhumi-marks-predictor.streamlit.app/
## 📌 About
This project uses a Linear Regression model trained on study-hours vs marks data to predict a student's expected score. Users enter their daily study hours (between 4–12) and get an instant predicted marks output, along with a visual progress indicator.

## 🛠️ Tech Stack
- **Python**
- **scikit-learn** — Linear Regression model
- **Streamlit** — web app / UI
- **Joblib** — model serialization

## ✨ Features
- Clean, card-based UI with custom CSS styling
- Real-time prediction based on study hours input
- Input validation (4–12 hours) with a styled warning message
- Visual progress bar showing predicted marks out of 100

## 🚀 Run Locally
```bash
pip install -r requirements.txt
streamlit run main.py
```

## 📊 Dataset
A simple study-hours-vs-marks dataset used to train a Linear Regression model, capturing the relationship between daily study time and academic performance.

## 🧠 What I Learned
- Training and serializing a regression model with scikit-learn
- Building an interactive ML-powered UI with Streamlit
- Designing a clean, distinct visual theme using custom CSS
- Structuring an end-to-end ML project for deployment
