import requests as r
import json


url = r.get("http://api.open-notify.org/astros.json").json()
with open("request.json", "w+") as f:
    json.dump(url, f, indent=4)
    print("wrote")
with open("request.json", "r+") as e:
    data = json.load(e)
    for line in data["people"]:
        print("Astronaut:", line["name"])
