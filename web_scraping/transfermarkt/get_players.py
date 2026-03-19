import requests
from bs4 import BeautifulSoup
import get_machine_headers
import json

headers = get_machine_headers.get_machine_headers()

with open("player-ids-to-names.json", "w") as f:
    f.write("[\n")

players = []

with open("club-ids-to-names.json", "r") as f:
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

with open("player-ids-to-names.json", "a") as f:
    for player in players:
        f.write(json.dumps(player) + ",\n")

with open("player-ids-to-names.json", "a") as f:
    f.write("]")