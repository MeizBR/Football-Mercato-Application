import requests
from bs4 import BeautifulSoup
import re
import pymongo
import os
import time
from pathlib import Path
from datetime import date

from dotenv import load_dotenv

load_dotenv()

import get_machine_headers

# host = os.environ.get("MONGODB_HOST")
# database = os.environ.get("MONGODB_DATABASE")
# user = os.environ.get("MONGODB_USER")
# password = os.environ.get("MONGODB_PASSWORD")

host = os.getenv("MONGODB_HOST")
database = os.getenv("MONGODB_DATABASE")
user = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

mydb = myclient["football-mercato"]

mycol = mydb["transfermarkt-rumours-news"]

headers = get_machine_headers.get_machine_headers()

current_dir = Path.home() / "Desktop" / "Football-Mercato-Application"

today = date.today()

player_names = []
club_names = []
player_market_values = []
player_joining_destinations = []
player_departure_clubs = []
tmp = []
rumours_list = []
scores = []
score_link_details = []
logs = []

def save_html_rumours_details(url, filename):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(current_dir / "rumours_details" / filename, "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        f.write("<h1>Failed to retrieve the page</h1>")

def get_rumours_function(headers, index):
    mycol.delete_many({})
    time.sleep(2)

    for i in range(1, index + 1):
        rumours_url = "https://www.transfermarkt.com/rumourmill/detail/forum/154/page/" + str(i) + "/"

        rumours_url_response = requests.get(
            rumours_url,
            headers=headers
        )

        soup = BeautifulSoup(rumours_url_response.text, "html.parser")

        for link in soup.select('a.tm-pagination__link'):
            href = link.get("href", "")

            match = re.search(r"/page/(\d+)", href)
            if match:
                page_number = int(match.group(1))

        for player_name in soup.select('div.spielername a'):
            player_names.append(player_name.text.strip())

        # print(player_names)

        for club_name in soup.select('div.vereinname a'):
            club_names.append(club_name.text.strip())

        # print(club_names)

        for player_market_value in soup.select('div.marktwertanzeige strong'):
            player_market_values.append(player_market_value.text.strip())

        # print(player_market_values)

        for player_joining_destination in soup.select('div.wechsel-verein-name a'):
            player_joining_destinations.append(player_joining_destination.text.strip())

        # print(player_joining_destinations)

        for player_departure_club in soup.select('div.gk-wappen a img'):
            player_departure_clubs.append(
                {
                    "club_name": player_departure_club.get("title", "").strip(),
                    "club_image_url": player_departure_club.get("src", "").strip()
                }
            )

        for i in range(0, len(player_departure_clubs), 2):
            tmp.append(
                {
                    "from": player_departure_clubs[i],
                    "to": player_departure_clubs[i+1]
                }
            )

        # print(tmp)

        for score in soup.select('div.geruecht-zahl'):
            if score:
                scores.append(score.text.strip() + " %")
            else:
                scores.append("0 %")

        for i, score_link_detail in enumerate(soup.select('a.link-zur-gk')):
            if score_link_detail:
                link = "https://www.transfermarkt.com" + score_link_detail.get("href", "").strip()
                score_link_details.append(link)
                
                # Optional safety check: ensure player_names has enough entries
                if i < len(player_names):
                    player_name = player_names[i].replace(' ', '_').lower()
                else:
                    player_name = f"unknown_player_{i}"

                save_html_rumours_details(link, f"{player_name}_rumour_{today}_details.html")
            else:
                score_link_details.append("No details available.")

        for i,j,k,l,m,n,o in zip(player_names, club_names, player_market_values, player_joining_destinations, tmp, scores, score_link_details):
            d = {
                    "player_name": i,
                    "current_club": j,
                    "market_value": k,
                    "joining_destination": l,
                    "departure_club": m["from"],
                    "arrival_club": m["to"],
                    "score": n,
                    "score_link_details": o
                }
            rumours_list.append(d)
            # x = mycol.insert_one(d)
            # logs.append(x.inserted_id)

    return [rumours_list, logs]

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    rumours_data, logs = get_rumours_function(headers, 50)

    print("Transfer news table:\n")
    for item in rumours_data:
        print(item)

    print("\nLogs:\n")
    for log in logs:
        print(log)