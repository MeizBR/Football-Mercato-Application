from bs4 import BeautifulSoup
import re
import requests
import json
from fastapi import FastAPI

import market_value_history
import transfer_history
import player_gallery
import get_machine_headers
import get_rumours

import player_details

from latest_transfers import premier_league

# Headers
headers = get_machine_headers.get_machine_headers()

app = FastAPI()

@app.get("/playerProfile/{player_name}/{player_id}/information")
def get_player(player_id: int, player_name: str):
    return {
        "player": {
            "id": player_details.get_player_details(player_id, player_name, headers)["player_name"],
            "name": player_details.get_player_details(player_id, player_name, headers)["player_name"],
            "number": player_details.get_player_details(player_id, player_name, headers)["player_number"],
            "market_value": player_details.get_player_details(player_id, player_name, headers)["player_market_value"].split(' ')[0],
            "market_value_last_update": player_details.get_player_details(player_id, player_name, headers)["player_market_value"].split(' ')[-1],
            "international_squad": player_details.get_player_details(player_id, player_name, headers)["player_international_squad"],
            "birthplace": player_details.get_player_details(player_id, player_name, headers)["player_birthplace"],
            "agent": player_details.get_player_details(player_id, player_name, headers)["player_agent"],
            "height": player_details.get_player_details(player_id, player_name, headers)["player_height"],
            "citizenship": player_details.get_player_details(player_id, player_name, headers)["player_citizenship"],
            "position": player_details.get_player_details(player_id, player_name, headers)["player_position"],
            "image_url": player_details.get_player_details(player_id, player_name, headers)["player_image_url"],
        },
    }

@app.get("/player/{player_name}/{player_id}/club")
def get_player(player_id: int, player_name: str):
    return {
        "club": {
            "club": player_details.get_player_club_details(player_id, player_name, headers)["player_club"],
            "league": player_details.get_player_club_details(player_id, player_name, headers)["club_league"],
            "club_league_level": player_details.get_player_club_details(player_id, player_name, headers)["player_club_league_level"].strip(),
            "club_image_url": f"https://tmssl.akamaized.net//images/wappen/head/{player_details.get_player_club_details(player_id, player_name, headers)['club_id']}.png",
            "joined_date": player_details.get_player_club_details(player_id, player_name, headers)["player_joined_date"],
            "contract_expiry": player_details.get_player_club_details(player_id, player_name, headers)["player_contract_expiry"],
        },
    }

@app.get("/player/{player_name}/{player_id}/furtherInformation")
def get_player(player_id: int, player_name: str):
    return {
        "further_information": {
                f"information {i+1}": player_details.get_player_details(player_id, player_name, headers)["player_further_information"][i] for i in range(len(player_details.get_player_details(player_id, player_name, headers)["player_further_information"]) - 1)
        },
    }

@app.get("/player/{player_id}/transferRumours")
def get_player(player_id: int):
    return {
        "rumours": {
                f"rumour {i+1}": {
                    "club": player_details.get_rumours(player_id, headers)[i]["club"],
                    "competition": player_details.get_rumours(player_id, headers)[i]["competition"]
                } for i in range(len(player_details.get_rumours(player_id, headers)))
        },
    }

# Unchanged endpoints below - still to work on refactoring them to be more efficient and less redundant

@app.get("/player/{player_id}/marketValueHistory")
def get_player(player_id: int):
    return {
        "market_value_history": {
                f"market_value_{i+1}": {
                    "amount": market_value_history.fetch_market_value_history(player_id, headers)[i]["amount"],
                    "currency": market_value_history.fetch_market_value_history(player_id, headers)[i]["currency"],
                    "date": market_value_history.fetch_market_value_history(player_id, headers)[i]["date"]
                } for i in range(len(market_value_history.fetch_market_value_history(player_id, headers)))
        },
    }

@app.get("/player/{player_id}/transferHistory")
def get_player(player_id: int):
    return {
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
        },
    }

@app.get("/player/{player_id}/gallery")
def get_player(player_id: int):
    return {
        "gallery": {
                f"image_{i+1}": {
                    "image_title": player_gallery.get_player_gallery(player_id, headers)[i]["image_title"],
                    "image_url": player_gallery.get_player_gallery(player_id, headers)[i]["image_url"],
                } for i in range(len(player_gallery.get_player_gallery(player_id, headers)))
        },
    }

@app.get("/rumours/page/{index}")
def rumours(index: int):
    return {
        "rumours": {
                f"rumour_{i+1}": {
                    "player_name": get_rumours.get_rumours_function(headers, index)[i]["player_name"],
                    "current_club": get_rumours.get_rumours_function(headers, index)[i]["current_club"],
                    "market_value": get_rumours.get_rumours_function(headers, index)[i]["market_value"],
                    "joining_destination": get_rumours.get_rumours_function(headers, index)[i]["joining_destination"],
                    "departure_club": get_rumours.get_rumours_function(headers, index)[i]["departure_club"],
                    "arrival_club": get_rumours.get_rumours_function(headers, index)[i]["arrival_club"]
                } for i in range(len(get_rumours.get_rumours_function(headers, index)))
        },
    }

@app.get("/latestTransfers")
def latest_transfers():
    return {
        "latestTransfers": {
                f"transfer_{i+1}": {
                    "player_name": premier_league.premier_league_transfers[i]["player_name"],
                    "player_position": premier_league.premier_league_transfers[i]["player_position"],
                    "player_image_url": premier_league.premier_league_transfers[i]["player_image_url"],
                    "country_name": premier_league.premier_league_transfers[i]["country_name"],
                    "country_image_url": premier_league.premier_league_transfers[i]["country_image_url"],
                    "transfer_fee": premier_league.premier_league_transfers[i]["transfer_fee"],
                    "departure_club": premier_league.premier_league_transfers[i]["departure_club"],
                    "joining_club": premier_league.premier_league_transfers[i]["joining_club"],
                } for i in range(len(premier_league.premier_league_transfers))
        },
    }