import discord
import json
import time
import requests as r


class Astronaut(discord.Client):
    async def on_ready(self):
        self.url = "http://api.open-notify.org/astros.json"
        print("Ready to gather space data!")
        print("Connection established: ", self.user)

    async def on_message(self, message):
        if message.content.startswith("!astronauts"):
            await message.channel.send("Beep beep, retrieving astronauts data!")
            await message.channel.send("Astronauts currently in space:")
            time.sleep(1)
            astrodata = r.get(self.url).json()
            with open("data/astronauts.json", "w+") as d:
                json.dump(astrodata, d, indent=4)
                print("Astronauts data succesfully dumped.")
            with open("data/astronauts.json", "r+") as e:
                self.astrodata = json.load(e)
                for line in self.astrodata["people"]:
                    self.astros = line["name"]
                    await message.channel.send("{}".format(self.astros))

        if message.content.startswith("!location"):
            await message.channel.send("Retrieving current ISS location:")
            time.sleep(1)
            self.location = r.get("http://api.open-notify.org/iss-now.json")
            self.location_json = self.location.json()
            with open("data/location.json", "w+") as l:
                json.dump(self.location_json, l, indent=4)
                print("Location data dumped.")
            with open("data/location.json", "r+") as d:
                self.location = json.load(d)
                self.longitude = self.location["iss_position"]["longitude"]
                self.latitude = self.location["iss_position"]["latitude"]
                await message.channel.send("Longitude: {}, Latitude: {}".format(self.longitude, self.latitude))


app = Astronaut()
app.run("token")
