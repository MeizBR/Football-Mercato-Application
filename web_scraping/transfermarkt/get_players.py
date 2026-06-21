import requests
from bs4 import BeautifulSoup
import get_machine_headers
import json
import pymongo
import os
import time
from dotenv import load_dotenv

import transfer_history, market_value_history, player_details, player_gallery

load_dotenv()

host = os.getenv("MONGODB_HOST")
database = os.getenv("MONGODB_DATABASE")
user = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

print(f"Host: {host}")
print(f"Database: {database}")
print(f"User: {user}")
print(f"Password: {password}")

print("database names:", myclient.list_database_names())

mydb = myclient["football-mercato"]

mycol = mydb["serie-a-players-list"]

headers = get_machine_headers.get_machine_headers()

with open("serie-a-list-of-clubs.json", "r") as f:
    players = []
    logs = []

    mycol = mydb["serie-a-players-list"]

    file = json.load(f)
    for club in file:

        response = requests.get(club["club_name_url"], headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.select("td.hauptlink a"):
            href = link.get("href", "")

            player_id = href[(href.find("/spieler") + 9):]
            player_name = href[1:href.find("/profil")]

            player = {
                "player_id": player_id,
                "player_name": player_name
            }

            if (player_id.isnumeric()) and (player_name.find("spieler") == -1):
                players.append(player)
            else:
                continue

        time.sleep(1)

    time.sleep(1) 

    for player in players:
        basic_details = player_details.get_player_details(player["player_id"], player["player_name"], headers)
        rumours = player_details.get_rumours(player["player_id"], headers)


        # transfer_hisotry_details = transfer_history.get_transfer_history(player["player_id"], headers)
        # market_value_history_details = market_value_history.fetch_market_value_history(player["player_id"], headers)
        # gallery_images = player_gallery.get_player_gallery(player["player_id"], headers)

        # player_object = {
        #     "basic_details": basic_details,
        #     "rumours": rumours,
        #     "transfer_hisotry_details": transfer_hisotry_details,
        #     "market_value_history_details": market_value_history_details,
        #     "gallery_images": gallery_images
        # }


        player_object = {
            "basic_details": basic_details,
            "rumours": rumours,
        }

        if (mycol.find_one({"basic_details.player_name": player_object["basic_details"]["player_name"]})):
            print(f"the player with id {player['player_id']} already exists in the database")
            continue
        else:
            x = mycol.insert_one(player_object)
            print(f"the player with id {x.inserted_id} was inserted")

        time.sleep(5)