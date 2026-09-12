# 📉 Customer Churn Prediction & Decision-Support Dashboard

An end-to-end machine learning system that predicts customer churn probability and provides actionable retention recommendations through an interactive dashboard.

## 🚀 Live Demo

**Streamlit Dashboard:**  
https://customer-churn-prediction-dashboard-wque9m5rrvyad7jchvyp6w.streamlit.app/

**FastAPI API:**  
https://customer-churn-prediction-dashboard-s2f0.onrender.com/

**API Documentation:**  
https://customer-churn-prediction-dashboard-s2f0.onrender.com/docs

---

## 🎯 Project Objective

Customer churn can significantly impact business revenue and customer lifetime value.

This project uses machine learning to:

- Predict whether a customer is likely to churn
- Estimate churn probability
- Classify customers into Low, Medium, and High risk
- Optimize the prediction threshold based on business cost
- Provide targeted retention recommendations
- Serve predictions through a production API
- Provide an interactive business dashboard

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      GitHub         │
                    │   Source Code       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
      ┌──────────────────┐          ┌──────────────────┐
      │ Streamlit Cloud  │          │      Render      │
      │    Dashboard     │─────────▶│     FastAPI      │
      └──────────────────┘          └────────┬─────────┘
                                             │
                                             ▼
                                  ┌────────────────────┐
                                  │ CatBoost Champion  │
                                  │       Model        │
                                  └────────────────────┘
