from fastapi import FastAPI
import pandas as pd 
from app.schemas import CustomerRequest
from app.config import THRESHOLD
from app.predictor import load_model


app = FastAPI()
model = load_model()


@app.get("/")
def root():
    return {"message": "Customer Churn API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(customer: CustomerRequest):

    customer_dict = customer.model_dump()

    customer_df = pd.DataFrame([customer_dict])

    prediction = model.predict(customer_df)

    probability_yes = float(prediction[0][1])

    churn_prediction = "Yes" if probability_yes >= THRESHOLD else "No"

    risk_level = (
        "High"
        if probability_yes >= 0.70
        else "Medium"
        if probability_yes >= THRESHOLD
        else "Low"
    )

    return {
        "churn_probability": round(probability_yes, 4),
        "threshold": THRESHOLD,
        "prediction": churn_prediction,
        "risk_level": risk_level,
    }