# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pandas as pd

# from src.pipelines.inference_pipeline import InferencePipeline

# # -------------------------------
# # Initialize App
# # -------------------------------
# app = FastAPI(
#     title="Car Resale Price Estimator API",
#     description="Predict car price using trained ML model",
#     version="1.0"
# )

# # Load pipeline once (important for performance)
# pipeline = InferencePipeline("config/config.yaml")


# # -------------------------------
# # Input Schema
# # -------------------------------
# class CarInput(BaseModel):
#     Car_Name: str
#     Year: int
#     Distance: int
#     Owner: int
#     Fuel: str
#     Location: str
#     Drive: str
#     Type: str


# # -------------------------------
# # Routes
# # -------------------------------
# @app.get("/")
# def home():
#     return {"message": "Car Price Prediction API is running 🚗"}


# @app.post("/predict")
# def predict(data: CarInput):
#     try:
#         # Convert input to DataFrame
#         df = pd.DataFrame([data.dict()])

#         # Make prediction
#         prediction = pipeline.predict(df)

#         # Convert NumPy type → Python float
#         price = float(prediction[0])

#         return {
#             "predicted_price": price
#         }

#     except Exception as e:
#         # Proper error handling
#         raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

from src.pipelines.inference_pipeline import (
    InferencePipeline
)

app = FastAPI()

pipeline = InferencePipeline(
    "config/config.yaml"
)


class CarInput(BaseModel):

    Car_Name: str
    Year: int
    Distance: int
    Owner: int
    Fuel: str
    Location: str
    Drive: str
    Type: str


@app.get("/")
def home():

    return {
        "message": "API Running"
    }


@app.post("/predict")
def predict(data: CarInput):

    try:

        df = pd.DataFrame([{
            "Car Name": data.Car_Name,
            "Year": data.Year,
            "Distance": data.Distance,
            "Owner": data.Owner,
            "Fuel": data.Fuel,
            "Location": data.Location,
            "Drive": data.Drive,
            "Type": data.Type
        }])

        prediction = pipeline.predict(df)

        return {
            "predicted_price": prediction[0]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )