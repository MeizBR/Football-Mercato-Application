import requests
from bs4 import BeautifulSoup
import re
import pymongo
import os
import time
import clubs_list

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

mycol = mydb["top-transfers-news"]

headers = get_machine_headers.get_machine_headers()

player_names = []
player_market_values = []
player_fees = []
player_departure_clubs = []
top_transfers_list = []
logs = []

def get_top_transfers_function(headers):
    # mycol.delete_many({})
    # time.sleep(2)

    top_transfers_url = "https://www.transfermarkt.com/statistik/saisontransfers"

    top_transfers_url_response = requests.get(
        top_transfers_url,
        headers=headers
    )

    soup = BeautifulSoup(top_transfers_url_response.text, "html.parser")

    for player_name in soup.select('tr.odd td.hauptlink a'):
        player_names.append(player_name.get("title", ""))

    for player_market_value in soup.select('tr.odd td.rechts'):
        player_market_values.append(player_market_value.text.strip())

    for player_fee in soup.select('tr.odd td.rechts.hauptlink.bg_gruen_20'):
        player_fees.append(player_fee.text.strip())

    for i,j,k in zip(player_names, player_market_values, player_fees):
        d = {
                "player_name": i,
                "market_value": j,
                "fees": k
            }
        top_transfers_list.append(d)

    i = 0

    while i < len(top_transfers_list):
        if top_transfers_list[i]["player_name"] in clubs_list.transfermarkt_european_clubs:
            top_transfers_list[i - 1]["current_club"] = top_transfers_list[i]["player_name"]
            top_transfers_list.pop(i)
        else:
            i += 1

        # x = mycol.insert_one(d)
        # logs.append(x.inserted_id)

    # return [top_transfers_list, logs]
    return top_transfers_list

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    top_transfers_data = get_top_transfers_function(headers=headers)

    print("Transfer news table:\n")
    for item in top_transfers_data:
        print(item)

    print("\nLogs:\n")
    for log in logs:
        print(log)