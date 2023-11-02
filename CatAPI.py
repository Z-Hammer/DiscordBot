import requests
import json

def get_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {"x-api-key": 'live_DNbPe9uJqyI9U2CuRhTebq3yOlRxKTniwhqHsyHaIZoagMg95by8nJFomWJBIsVb'}
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    if response.status_code == 200:
        cat_image_url = data[0]['url']
        return (cat_image_url)
    else:
        return ('Failed')
