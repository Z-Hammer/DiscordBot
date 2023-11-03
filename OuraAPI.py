import requests 
import json

def oura_data(p_message):
    url = 'https://api.ouraring.com/v2/usercollection/daily_readiness'
    url2 = 'https://api.ouraring.com/v2/usercollection/daily_activity' 
    params={ 
        'start_date': p_message,
        'end_date': p_message
    }
    headers = { 
        'Authorization': 'Bearer Token' 
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    response2 = requests.request('GET', url2, headers=headers, params=params) 
    data = response.json()
    data2 = response2.json()
    Errors = [False , False]
    try:
        data['data'][0]
    except:
        Errors[0] = True
    try:
        data2['data'][0]
    except:
        Errors[1] = True
    
    if Errors[0] != True and Errors[1] != True:
        return (f"Day: {data2['data'][0]['day']}\n"
                f"Score: {data2['data'][0]['score']} out of 100\n"
                f"Steps: {data2['data'][0]['steps']}\n"
                f"Active Cal: {data2['data'][0]['active_calories']}\n"
                f"Temperature Deviation: {data['data'][0]['temperature_deviation']}\n"
                f"Body Temp: {data['data'][0]['contributors']['body_temperature']} out of 100\n"
                f"HRV Balance: {data['data'][0]['contributors']['hrv_balance']} out of 100\n"
                f"Resting HR: {data['data'][0]['contributors']['resting_heart_rate']} out of 100\n"
                f"Sleep Score: {data['data'][0]['contributors']['sleep_balance']} out of 100"
                )
    elif Errors[0] != True and Errors[1] != False:
        return (f"Day: {p_message}\n"
                f"Temperature Deviation: {data['data'][0]['temperature_deviation']}\n"
                f"Body Temp: {data['data'][0]['contributors']['body_temperature']} out of 100\n"
                f"HRV Balance: {data['data'][0]['contributors']['hrv_balance']} out of 100\n"
                f"Resting HR: {data['data'][0]['contributors']['resting_heart_rate']} out of 100\n"
                f"Sleep Score: {data['data'][0]['contributors']['sleep_balance']} out of 100"
                )
    elif Errors[0] != False and Errors[1] != True:
        return (f"Day: {data2['data'][0]['day']}\n"
                f"Score: {data2['data'][0]['score']} out of 100\n"
                f"Steps: {data2['data'][0]['steps']}\n"
                f"Active Cal: {data2['data'][0]['active_calories']}\n"
                )
    else:
        return('')
