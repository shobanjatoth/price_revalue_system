from fastapi import FastAPI
import pandas as pd

from src.pipelines.inference_pipeline import InferencePipeline

app = FastAPI()

pipeline = InferencePipeline("config/config.yaml")


@app.get("/")
def home():
    return {"message": "Car Price Prediction API"}


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = pipeline.predict(df)

    return {"prediction": float(prediction[0])}
