from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_predict_endpoint():

    payload = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "No",
        "MultipleLines": "No phone service",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 29.85,
        "TotalCharges": 29.85
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert 0 <= data["churn_probability"] <= 1
    assert data["prediction"] in ["Yes", "No"]
    assert data["risk_level"] in ["Low", "Medium", "High"]

    assert "churn_probability" in data
    assert "prediction" in data
    assert "risk_level" in data


def test_predict_invalid_input():

    payload = {
        "gender": "Female",
        "SeniorCitizen": "INVALID_VALUE"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422    