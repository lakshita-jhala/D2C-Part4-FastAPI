from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class CustomerData(BaseModel):
    city_tier: str
    age_group: str
    acquisition_channel: str
    loyalty_tier: str
    preferred_category: str
    marketing_consent: int
    recency_days: float
    frequency_180d: float
    monetary_180d: float
    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float
    category_diversity_180d: float
    ticket_count_90d: float
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float
    days_since_signup: float
    sessions_30d: float
    product_views_30d: float
    cart_adds_30d: float
    wishlist_adds_30d: float
    abandoned_carts_30d: float
    email_opens_30d: float
    campaign_clicks_30d: float
    last_visit_days_ago: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(customer: CustomerData):

    df = pd.DataFrame([customer.dict()])

    prob = float(model.predict_proba(df)[0][1])

    pred = int(prob >= 0.5)

    risk = "high" if prob >= 0.7 else "medium" if prob >= 0.4 else "low"

    return {
        "churn_probability": round(prob,4),
        "predicted_class": pred,
        "risk_level": risk,
        "risk_explanation": "Prediction generated using customer behavior and engagement features."
    }

@app.post("/batch_predict")
def batch_predict(customers: list[CustomerData]):

    df = pd.DataFrame([c.dict() for c in customers])

    probs = model.predict_proba(df)[:,1]

    preds = (probs >= 0.5).astype(int)

    results = []

    for p,pred in zip(probs,preds):
        results.append({
            "churn_probability": round(float(p),4),
            "predicted_class": int(pred)
        })

    return {"predictions": results}

