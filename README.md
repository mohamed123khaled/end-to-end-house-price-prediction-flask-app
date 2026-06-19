# 🏠 Bangalore House Price Prediction System

An end-to-end Machine Learning web application for predicting real estate prices in Bangalore using a trained regression model and a Flask backend with a dynamic frontend interface.

---

## 📌 Project Overview

This project is a full-stack Machine Learning application that predicts house prices based on:

* Total area (sqft)
* Number of BHK
* Number of bathrooms
* Location in Bangalore

It includes both:

* Machine Learning model (trained offline)
* Flask backend API
* Interactive HTML/CSS/JavaScript frontend

---

## ⚙️ Tech Stack

* Python
* Flask
* Scikit-Learn
* NumPy
* Pandas
* HTML / CSS / JavaScript
* jQuery
* Pickle (Model Serialization)

---

## 🧠 Machine Learning Pipeline

The model was trained using:

* Data Cleaning & Preprocessing
* One-Hot Encoding for locations
* Feature Engineering
* Linear Regression Model
* Model Serialization using Pickle

---

## 🌐 System Architecture

User Input (Frontend)
→ JavaScript (AJAX Request)
→ Flask API
→ ML Model Prediction
→ Response (Estimated Price)

---

## 🚀 Features

* Real-time price prediction
* Dynamic location dropdown
* REST API using Flask
* Clean UI design
* Fast response time
* Ready-to-run local deployment

---

## 📁 Project Structure

```text
├── app.py                  # Flask backend server
├── util.py                 # Model loading & prediction logic
├── columns.json           # Feature columns metadata
├── model.pickle           # Trained ML model
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   └── app.css            # Styling
└── README.md
```

---

## 🔥 How to Run

```bash
# 1. Install dependencies
pip install flask numpy pandas scikit-learn

# 2. Run Flask server
python app.py

# 3. Open browser
http://127.0.0.1:5001/
```

---

## 📊 Model Details

* Algorithm: Linear Regression
* Output: House Price (Lakhs)
* Input Features: Area, BHK, Bathrooms, Location
* Encoding: One-Hot Encoding

---

## 🎯 Key Highlights

* End-to-End Machine Learning Deployment
* Real-time API using Flask
* Dynamic frontend integration
* Production-style project structure
* Clean modular ML pipeline

---

## 👨‍💻 Author

Mohamed Khaled
Machine Learning & Data Science Enthusiast

---

## 📌 Note

This project demonstrates full-cycle ML deployment from training to production-like API integration.
