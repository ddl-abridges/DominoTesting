import mlflow
import os

def show_models():
    client = mlflow.MlflowClient()
    data = client.search_registered_models()
    print(os.environ['DOMINO_USER_API_KEY'])
    return data