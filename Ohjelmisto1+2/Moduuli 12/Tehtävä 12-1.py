import requests

pyyntö = "https://api.chucknorris.io/jokes/random"
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        print(vastaus.json()["value"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")

