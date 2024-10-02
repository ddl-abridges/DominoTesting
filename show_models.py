import os

def show_models():
    url = "https://sup5101ab.support-team-sandbox.domino.tech/api/registeredmodels/v1"
    payload = {}
    headers = {
      'X-Domino-Api-Key': os.environ['DOMINO_API_KEY']
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)