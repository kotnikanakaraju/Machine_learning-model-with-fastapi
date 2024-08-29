from fastapi import FastAPI
from pydantic import BaseModel 
import joblib 
import numpy as np

model=joblib.load('model.pkl')

app =FastAPI()

class PredictRequest(BaseModel):
    sepal_length:float
    sepal_width:float
    petal_lenght:float
    petal_width:float

@app.post("/predict")
def predict(request:PredictRequest):
    data=np.array([
        [request.sepal_length, request.sepal_width, request.petal_lenght, request.petal_width]
    ])
    prediction=model.predict(data)
    species_map={0:'setosa',1:'versicolor',2:'virginica'}
    return {"prediction":species_map[int(prediction[0])]}

@app.get("/")
def read_root():
    return {"message":"hello world"}
