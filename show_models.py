import mlflow
import os

from mlflow.tracking.request_header.abstract_request_header_provider import RequestHeaderProvider 
from mlflow.tracking.request_header.registry import _request_header_provider_registry 

class DominoApiKeyRequestHeaderProvider(RequestHeaderProvider): 
    """ 
    Provides X-Domino-Api-Key request header. 
    """ 

    def __init__(self): 
        self._domino_api_key = os.environ['DOMINO_API_KEY']

    def in_context(self): 
        return self._domino_api_key is not None 

    def request_headers(self): 
        request_headers = {} 

        if self._domino_api_key is not None: 
            request_headers["X-Domino-Api-Key"] = self._domino_api_key 

        return request_headers 
    

def show_models():
    _request_header_provider_registry.register(DominoApiKeyRequestHeaderProvider) 
    
    # Set MLFlow tracking URI 
    mlflow_tracking_uri = os.environ['MLFLOW_TRACKING_URI'] 
    mlflow.set_tracking_uri(mlflow_tracking_uri) 

    client = mlflow.MlflowClient()
    data = client.search_registered_models()
    return data