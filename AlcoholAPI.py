import requests
import json

def get_alcohol():
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    together = ""
    measurements = []
    ingredients = []
    drink = data['drinks'][0]
    for i in range(1, 10):
        if drink[f'strIngredient{i}'] == None:
            break
        else:
            ingredients.append(drink[f'strIngredient{i}'])
    
    for i in range(1, 10):
        if drink[f'strMeasure{i}'] == None:
            break
        else:
            measurements.append(drink[f'strMeasure{i}'])
    
    for i in range(len(ingredients)):
        try:
            together = together + (f"{ingredients[i]}   {measurements[i]}\n")
        except:
            together = together + (f"{ingredients[i]}   N/A\n")

    if response.status_code == 200:
        return(f"{drink['strDrink']}\n\n{together}\n{drink['strInstructions']}")
    else:
        return False