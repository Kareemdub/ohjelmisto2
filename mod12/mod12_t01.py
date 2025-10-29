import requests
import json

#hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto = "https://api.chucknorris.io/jokes/random"
try:
    vastaus = requests.get(pyynto)
    print("Status code: ", vastaus.status_code)
    if vastaus.status_code == 200:
        data = vastaus.json()
        print(data['value'])

except requests.exceptions.RequestException as e:
    print("virhe")








