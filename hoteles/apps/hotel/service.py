import requests
from requests.models import Response

def get_sentiment(text):

    url = 'http://localhost:3030/classifier/'
    data= {"text" : text}
    print(data)
    response = requests.post(url,json = data)
    if response.status_code == 200:
        r =response.json()
        if r['label']=='positivo':
            return True
        if r['label']=='negativo':
            return False