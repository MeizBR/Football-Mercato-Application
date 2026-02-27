from bs4 import BeautifulSoup
import re
import requests
import json
from fastapi import FastAPI

import market_value_history
import transfer_history

# Windows headers
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
# }

# Linux headers
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

player_id = 566799
player_name = "james-trafford"
url = "https://www.transfermarkt.com/" + player_name + "/profil/spieler/" + str(player_id)

print(f"Fetching data for player Name: {player_name}, Player ID: {player_id} from URL: {url}")

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

player_name = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
player_number = soup.select_one('span[class="data-header__shirt-number"]').text.strip().replace('#', '')
player_club = soup.select_one('span[class="data-header__club"]').text.strip()
club_league = soup.select_one('span[class="data-header__league"]').text.strip()
player_club_league_level = re.search("League level:\s*(.*)", soup.text).group(1)
player_international_squad = re.search("Current international:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()

print(f"Player ID: {player_id}")
print(f"Player Name: {player_name}")
print(f"Player Number: {player_number}")
print(f"Player Club: {player_club}")
print(f"Club League: {club_league}")
print(f"Player Club League Level: {player_club_league_level}")
print(f"Player International Squad: {player_international_squad}")


print("Current Rumours:")

club_rumour_url = "https://www.transfermarkt.com/ceapi/currentRumors/player/" + str(player_id) + "/"

club_rumour = requests.get(
        club_rumour_url,
        headers=headers
).json()

rumours = []

rumors = club_rumour["rumors"]
for rumor in rumors:
    club = rumor["club"]
    name = club["name"]
    competition = club["competitionName"]

    print(f"Club: {name}, Competition: {competition}")
    rumours.append({
        "club": name,
        "competition": competition
    })


player_joined_date = re.search("Joined: (.*)", soup.text).group(1)
player_contract_expiry = re.search("Contract expires: (.*)", soup.text).group(1)
player_birthplace = re.search("Place of birth:.*?([A-z].*?) ", soup.text, re.DOTALL).group(1).strip()
player_agent = re.search("Agent:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()
player_height = re.search("Height:.*?([0-9].*?)\n", soup.text, re.DOTALL).group(1).strip()
player_citizenship = re.search("Citizenship:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()
player_position = re.search("Position:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()

print(f"Player Joined Date: {player_joined_date}")
print(f"Player Contract Expiry: {player_contract_expiry}")
print(f"Player Birthplace: {player_birthplace}")
print(f"Player Agent: {player_agent}")
print(f"Player Height: {player_height}")
print(f"Player Citizenship: {player_citizenship}")
print(f"Player Position: {player_position}")

player_img = soup.select_one('img[class="data-header__profile-image"]')
player_image_url = player_img['src']
print(f"Player Image URL: {player_image_url}")

player_further_information = soup.select_one('div[class="content"]').text.strip()
player_further_information_list = player_further_information.split('.')
print(f"Player Further Information: {player_further_information_list}")

# Print the name of the club from the given id
club_id = 0
with open("club-ids-to-names.json", "r") as f:
    club_ids_to_names = json.load(f)
    for club in club_ids_to_names:
        if club["club_name"] == player_club:
            club_id = club["club_id"]




app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/player/{player_id}")
def get_player(player_id: int):
    return {
        "player": {
            "id": player_id,
            "name": player_name,
            "number": player_number,
            "international_squad": player_international_squad,
            "birthplace": player_birthplace,
            "agent": player_agent,
            "height": player_height,
            "citizenship": player_citizenship,
            "position": player_position,
            "image_url": player_image_url,
        },
        "club": {
            "club": player_club,
            "league": club_league,
            "club_league_level": player_club_league_level.strip(),
            "club_image_url": f"https://tmssl.akamaized.net//images/wappen/head/{club_id}.png",
            "joined_date": player_joined_date,
            "contract_expiry": player_contract_expiry,
        },
        "further_information": {
                f"information {i+1}": player_further_information_list[i] for i in range(len(player_further_information_list) - 1)
        },
        "rumours": {
                f"rumour {i+1}": {
                    "club": rumours[i]["club"],
                    "competition": rumours[i]["competition"]
                } for i in range(len(rumours))
        },
        "market_value_history": {
                f"market_value_{i+1}": {
                    "amount": market_value_history.fetch_market_value_history(player_id, headers)[i]["amount"],
                    "currency": market_value_history.fetch_market_value_history(player_id, headers)[i]["currency"],
                    "date": market_value_history.fetch_market_value_history(player_id, headers)[i]["date"]
                } for i in range(len(market_value_history.fetch_market_value_history(player_id, headers)))
        },
        "transfer_history" : {
                f"transfer_{i+1}": {
                    "transfer_source": {
                        "competition_id": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_source"]["competition_id"],
                        "country_id": transfer_history.get_transfer_history(player_id, headers)[i]
                        ["transfer_source"]["country_id"],
                        "country_flag": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_source"]["country_flag"],
                        "club_id": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_source"]["club_id"],
                        "club_logo": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_source"]["club_logo"],
                    },
                    "transfer_destination": {
                        "competition_id": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_destination"]["competition_id"],
                        "country_id": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_destination"]["country_id"],
                        "country_flag": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_destination"]["country_flag"],
                        "club_id": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_destination"]["club_id"],
                        "club_logo": transfer_history.get_transfer_history(player_id, headers)[i]["transfer_destination"]["club_logo"],
                    },
                    "date": transfer_history.get_transfer_history(player_id, headers)[i]["date"],
                    "contract_until_date": transfer_history.get_transfer_history(player_id, headers)[i]["contract_until_date"],
                    "season_id": transfer_history.get_transfer_history(player_id, headers)[i]["season_id"],
                    "market_value": {
                        "amount": transfer_history.get_transfer_history(player_id, headers)[i]["market_value"]["amount"],
                        "currency": transfer_history.get_transfer_history(player_id, headers)[i]["market_value"]["currency"],
                    },
                    "fee" : {
                        "amount": transfer_history.get_transfer_history(player_id, headers)[i]["fee"]["amount"],
                        "currency": transfer_history.get_transfer_history(player_id, headers)[i]["fee"]["currency"],
                    }
                } for i in range(len(transfer_history.get_transfer_history(player_id, headers)))
        }
    }