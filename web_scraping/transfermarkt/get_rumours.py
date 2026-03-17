import requests
from bs4 import BeautifulSoup
import re
import pymongo
import os

host = os.environ.get("MONGODB_HOST")
database = os.environ.get("MONGODB_DATABASE")
user = os.environ.get("MONGODB_USER")
password = os.environ.get("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

mydb = myclient["football-mercato"]

mycol = mydb["transfermarkt-rumours-news"]

player_names = []
club_names = []
player_market_values = []
player_joining_destinations = []
player_departure_clubs = []
tmp = []
rumours_list = []
logs = []

def get_rumours_function(headers, index):
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

        for i,j,k,l,m in zip(player_names, club_names, player_market_values, player_joining_destinations, tmp):
            d = {
                    "player_name": i,
                    "current_club": j,
                    "market_value": k,
                    "joining_destination": l,
                    "departure_club": m["from"],
                    "arrival_club": m["to"]
                }
            rumours_list.append(d)
            x = mycol.insert_one(d)
            logs.append(x.inserted_id)

        # print(rumours_list [:2])
    return rumours_list, logs

# print(get_rumours_function(headers, 1))
if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    rumours_data, logs = get_rumours_function(headers, 2)

    print("Transfer news table:\n")
    for item in rumours_data:
        print(item)

    print("\nLogs:\n")
    for log in logs:
        print(log)