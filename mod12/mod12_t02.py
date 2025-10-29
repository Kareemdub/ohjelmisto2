import requests
import json
# my apikey 6c82236fac9786a882813e66d2807c74
API_key = "6c82236fac9786a882813e66d2807c74"
city_name = input("Anna Kaupunki, josta haluat säätiedot:")
lang = "fi"

try:
    city_call = (f"http://api.openweathermap.org/data/2.5/weather?q="
                 f"{city_name},&units=metric&lang={lang}&appid={API_key}")
    city_response = requests.get(city_call)
    print("Status code: ", city_response.status_code)
    if city_response.status_code == 200:
        data_city = city_response.json()
        print(json.dumps(data_city, indent=2))
        print(f"Sää kohteesa {city_name} on {data_city["weather"][0]['description']}")



except requests.exceptions.RequestException as e:
   print("virhe")







