import requests
from bs4 import BeautifulSoup
import re

def get_player_id(s):
    for i in range(55, len(s)):
        if s[i] == "-":
            break
    return s[55:i]

def get_ligue_1_transfers(headers):
    rumours_url = "https://www.transfermarkt.com/transfers/neuestetransfers/statistik/plus/?plus=0&galerie=0&wettbewerb_id=FR1&verein_land_id=&selectedOptionInternalType=nothingSelected&land_id=&minMarktwert=500.000&maxMarktwert=500.000.000&minAbloese=0&maxAbloese=500.000.000&yt0=Show"

    latest_transfers_url_response = requests.get(
        rumours_url,
        headers=headers
    )

    soup = BeautifulSoup(latest_transfers_url_response.text, "html.parser")

    player_details = []
    for element in soup.select('td img.bilderrahmen-fixed'):

        ext_id = get_player_id(element.get("data-src", "").strip())
        ext_name = element.get("alt", "").strip().lower().replace(" ", "-")

        ext_player_url = "https://www.transfermarkt.com/" + ext_name + "/profil/spieler/" + ext_id

        ext_response = requests.get(ext_player_url, headers=headers)

        ext_soup = BeautifulSoup(ext_response.content, "html.parser")

        player_details.append(
            {
                "player_name": element.get("alt", "").strip(),
                "player_position": re.search("Position:.*?([A-z].*?)\n", ext_soup.text, re.DOTALL).group(1).strip() if re.search("Position:.*?([A-z].*?)\n", ext_soup.text, re.DOTALL) else "Unknown",
                "player_image_url": element.get("data-src", "").strip(),
            }
        )

    # print(player_details)

    country_details = []
    for element in soup.select('td.zentriert img.flaggenrahmen'):
        country_details.append(
            {
                "country_name": element.get("alt", "").strip(),
                "country_image_url": element.get("src", "").strip()
            }
        )

    # print(country_details)

    player_departure_clubs = []
    for element in soup.select('img.tiny_wappen'):
        player_departure_clubs.append(
            {
                "club_name": element.get("alt", "").strip(),
                "club_image_url": element.get("src", "").strip()
            }
        )

    # print(player_departure_clubs)

    player_fees = []
    for element in soup.select('td.rechts a'):
        player_fees.append(element.text.strip())

    # print(player_fees)

    tmp = []
    for i in range(0, len(player_departure_clubs), 2):
        tmp.append(
            {
                "from": player_departure_clubs[i],
                "to": player_departure_clubs[i+1]
            }
        )

    # print(tmp)

    ligue_1_transfers = []
    for i,j,k,l in zip(player_details, country_details, player_fees, tmp):
        ligue_1_transfers.append(
            {
                "player_name": i["player_name"],
                "player_position": i["player_position"],
                "player_image_url": i["player_image_url"],
                "country_name": j["country_name"],
                "country_image_url": j["country_image_url"],
                "transfer_fee": k,
                "departure_club": l["from"],
                "joining_club": l["to"]
            }
        )

    return ligue_1_transfers