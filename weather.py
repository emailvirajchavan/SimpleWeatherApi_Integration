#open weather api tutorial 

import json
import requests

# API to fetch city weather
CityName = input("enter a city name: ")

ApiKey = 'a41e17b419b2a2ea4513f9842a5e6fa7'

# to build the API url
ApiUrl = f'https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid={ApiKey}&units=metric'



GetInformation = requests.get(ApiUrl)

if GetInformation.status_code == 200:
    data = GetInformation.json()

# print(json.dumps(GetInformation.json()))


# to fetch specific data from the JSON

    D = data["weather"][0]["description"]
    T = data["main"]["temp"]
    H = data["main"]["humidity"]  

    print(f"The weather in the {CityName} is {D} and the tempreature is {T} degree celsius and humidity is {H}")
    # print(GetInformation.status_code)
else:
    print("Failed to fetch data")




