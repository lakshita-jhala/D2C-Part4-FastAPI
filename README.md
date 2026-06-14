
# D2C Part 4 - FastAPI Churn Prediction Service

## Project Overview
This project provides a FastAPI API for customer churn prediction using a trained Logistic Regression model.

## Project Structure

app/main.py
tests/test_api.py
model.pkl
requirements.txt
monitoring_plan.md

## Installation

pip install -r requirements.txt

## Run API

uvicorn app.main:app --reload

## Endpoints

GET /health

POST /predict

POST /batch_predict

## Testing

pytest tests/

## Model Information

Model: Logistic Regression

Source: Part 3 Churn Prediction Model
