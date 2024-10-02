import mlflow

def show_models():
    client = mlflow.MlflowClient()
    data = client.search_registered_models()
    return data