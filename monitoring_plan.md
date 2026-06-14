
# Monitoring Plan

## Data Drift
Monitor changes in customer features such as:
- recency_days
- frequency_180d
- monetary_180d
- sessions_30d

## Prediction Distribution
Track:
- Percentage predicted as churn
- Average churn probability

## Business Outcomes
Track:
- Actual churn rate
- Retention campaign success rate

## API Monitoring
Track:
- Request count
- Response time
- Failed requests

## Retraining Triggers
Retrain the model when:
- Data drift becomes significant
- Prediction distribution changes substantially
- Model performance drops
