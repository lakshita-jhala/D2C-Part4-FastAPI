
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

sample_customer = {
    "city_tier":"Tier1",
    "age_group":"26-35",
    "acquisition_channel":"Organic",
    "loyalty_tier":"Gold",
    "preferred_category":"Electronics",
    "marketing_consent":1,
    "recency_days":10,
    "frequency_180d":5,
    "monetary_180d":10000,
    "return_rate_180d":0.1,
    "avg_discount_pct_180d":15,
    "avg_rating_180d":4.5,
    "category_diversity_180d":3,
    "ticket_count_90d":1,
    "negative_ticket_rate_90d":0,
    "avg_resolution_hours_90d":12,
    "days_since_signup":300,
    "sessions_30d":20,
    "product_views_30d":40,
    "cart_adds_30d":10,
    "wishlist_adds_30d":5,
    "abandoned_carts_30d":1,
    "email_opens_30d":8,
    "campaign_clicks_30d":3,
    "last_visit_days_ago":2
}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_predict():
    response = client.post("/predict", json=sample_customer)
    assert response.status_code == 200

def test_batch_predict():
    response = client.post(
        "/batch_predict",
        json=[sample_customer, sample_customer]
    )
    assert response.status_code == 200
