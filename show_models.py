import mlflow
import os

def show_models():
    client = mlflow.MlflowClient()
    data = client.search_registered_models()
    print(os.environ['MLFLOW_TRACKING_URI'])
    return data