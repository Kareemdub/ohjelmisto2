from tkinter.messagebox import showerror

import requests
import json

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls

pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyynto).json()
print(json.dumps(vastaus[0], indent=2))

#vastaus[0]["show"]["name"] = "Talo"
print(vastaus[0]["show"]["name"])

i = 0
for sarja in vastaus:

    if not vastaus[i]["show"]["genres"] == " ":
        print(f"Sarjan {vastaus[i]['show']['name']} arvostelu on pisteet ovat {vastaus[i]["score"]} ja "
              f"sarjan genret ovat {vastaus[i]['show']['genres']} ")

        i = i + 1




import requests
import json