from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from model_training import train_big_mart
from model_training import train_housing
from model_prediction import predict_big_mart
from model_prediction import predict_housing
import json

app = FastAPI()

class DataSet(BaseModel):
    dataset_name: str

class DataSample(BaseModel):
    dataset_name: str
    sample: dict

@app.post('/train')
def train_model(dataset: DataSet):
    dataset_name = dataset.dataset_name

    if dataset_name=='Big Mart Sales':
        summary = train_big_mart()

    elif dataset_name=='House Price':
        summary = train_housing()

    return {'summary':summary}

@app.post('/predict')
def predict_data(dataSample: DataSample):
    dataset_name = dataSample.dataset_name
    data = dataSample.sample

    if dataset_name=='Big Mart Sales':
        summary = predict_big_mart(data)

    elif dataset_name=='House Price':
        summary = predict_housing(data)

    return {'summary':summary}


# if this file is being executed then run the service
if __name__ == '__main__':
    # run the service uvicorn.run("filename:app")
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
    # http://localhost:8081/docs
    # uvicorn app:app --host 127.0.0.1 --port 8000 --reload