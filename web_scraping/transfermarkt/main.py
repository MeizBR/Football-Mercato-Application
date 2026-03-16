from fastapi import FastAPI

import market_value_history
import transfer_history
import player_gallery
import get_machine_headers
import get_rumours

import player_details

from latest_transfers import premier_league, la_liga, serie_a, bundesliga, ligue_1, liga_portugal, eredivisie, jupiler_pro_league, super_lig, eliteserien, allsvenskan, super_league, super_liga

from tuttomercato import main

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
    rumours = get_rumours.get_rumours_function(headers, index)

    return {
        "rumours": {
                f"rumour_{i+1}": {
                    "player_name": rumour["player_name"],
                    "current_club": rumour["current_club"],
                    "market_value": rumour["market_value"],
                    "joining_destination": rumour["joining_destination"],
                    "departure_club": rumour["departure_club"],
                    "arrival_club": rumour["arrival_club"]
                } for i, rumour in enumerate(rumours)
        },
    }

# Latest Premier League Transfers
@app.get("/premierLeague/latestTransfers")
def latest_transfers():
    transfers = premier_league.get_premier_league_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest La Liga Transfers
@app.get("/laLiga/latestTransfers")
def latest_transfers():
    transfers = la_liga.get_la_liga_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Serie A Transfers
@app.get("/serieA/latestTransfers")
def latest_transfers():
    transfers = serie_a.get_serie_a_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Bundesliga Transfers
@app.get("/bundesliga/latestTransfers")
def latest_transfers():
    transfers = bundesliga.get_bundesliga_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Ligue 1 Transfers
@app.get("/ligue1/latestTransfers")
def latest_transfers():
    transfers = ligue_1.get_ligue_1_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Liga Portugal Transfers
@app.get("/ligaPortugal/latestTransfers")
def latest_transfers():
    transfers = liga_portugal.get_liga_portugal_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Eredivisie Transfers
@app.get("/eredivisie/latestTransfers")
def latest_transfers():
    transfers = eredivisie.get_eredivisie_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Jupiler Pro League Transfers
@app.get("/jupilerProLeague/latestTransfers")
def latest_transfers():
    transfers = jupiler_pro_league.get_jupiler_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Super Lig Transfers
@app.get("/superLig/latestTransfers")
def latest_transfers():
    transfers = super_lig.get_super_lig_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Eliteserien Transfers
@app.get("/eliteserien/latestTransfers")
def latest_transfers():
    transfers = eliteserien.get_eliteserien_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Allsvenskan Transfers
@app.get("/allsvenskan/latestTransfers")
def latest_transfers():
    transfers = allsvenskan.get_allsvenskan_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Super League Transfers
@app.get("/superLeague/latestTransfers")
def latest_transfers():
    transfers = super_league.get_super_league_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Latest Super Liga Transfers
@app.get("/superLiga/latestTransfers")
def latest_transfers():
    transfers = super_liga.get_super_liga_transfers(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "player_name": transfer["player_name"],
                "player_position": transfer["player_position"],
                "player_image_url": transfer["player_image_url"],
                "country_name": transfer["country_name"],
                "country_image_url": transfer["country_image_url"],
                "transfer_fee": transfer["transfer_fee"],
                "departure_club": transfer["departure_club"],
                "joining_club": transfer["joining_club"],
            }
            for i, transfer in enumerate(transfers)
        }
    }

# Tuttomercato latest Transfers
@app.get("/tuttomercato/latestNews")
def latest_transfers():
    transfers = main.get_transfers_tuttomercato(headers)

    return {
        "latestTransfers": {
            f"transfer_{i+1}": {
                "date": transfer["date"],
                "detail": transfer["detail"]
            }
            for i, transfer in enumerate(transfers)
        }
    }