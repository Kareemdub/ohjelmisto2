import requests
import json
# my apikey 6c82236fac9786a882813e66d2807c74
API_key = "6c82236fac9786a882813e66d2807c74"
city_name = input("Anna Kaupunki, josta haluat säätiedot:")
lang = "fi"
lon = ""
lat = ""
city_call1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}"

try:
    city_response = requests.get(city_call1)
    #print("Status code: ", city_response.status_code)
    if city_response.status_code == 200:
        data_city1 = city_response.json()
       #print(json.dumps(data_city1, indent=2))
        eka = data_city1[0]
        lat, lon = eka["lat"], eka["lon"]
        #print(f"kaupunging {city_name} leveysaste on {lat} ja pituusaste {lon}")
except requests.exceptions.RequestException as e:
   print("virhe")


city_call2 = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
              f"&lang=fi")
try:

    city_response2 = requests.get(city_call2)
    #print("Status code: ", city_response2.status_code)
    if city_response2.status_code == 200:
        data_city2 = city_response2.json()
        #print(json.dumps(data_city2, indent=2))
        print(f"Sää kohteesa {city_name} on: {data_city2["weather"][0]['description']} "
              f"\nlämpötila on: {data_city2['main']['temp']} celsiusta")



except requests.exceptions.RequestException as e:
   print("virhe")




