from bs4 import BeautifulSoup
import re
import requests
import json

def get_player_details(player_id, player_name, headers):
    url = "https://www.transfermarkt.com/" + player_name + "/profil/spieler/" + str(player_id)
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    player_name = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
    player_number = soup.select_one('span[class="data-header__shirt-number"]').text.strip().replace('#', '')
    player_market_value = soup.select_one('a[class="data-header__market-value-wrapper"]').text.strip()

    player_club = soup.select_one('span[class="data-header__club"]').text.strip()
    club_league = soup.select_one('span[class="data-header__league"]').text.strip()
    player_club_league_level = re.search("League level:\s*(.*)", soup.text).group(1)
    player_international_squad = re.search("Current international:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()

    player_birthplace = re.search("Place of birth:.*?([A-z].*?) ", soup.text, re.DOTALL).group(1).strip()
    player_agent = re.search("Agent:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()
    player_height = re.search("Height:.*?([0-9].*?)\n", soup.text, re.DOTALL).group(1).strip()
    player_citizenship = re.search("Citizenship:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()
    player_position = re.search("Position:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()

    player_img = soup.select_one('img[class="data-header__profile-image"]')
    player_image_url = player_img['src']

    player_further_information = soup.select_one('div[class="content"]').text.strip()
    player_further_information_list = player_further_information.split('.')

    player_details = {
        "player_name": player_name,
        "player_number": player_number,
        "player_market_value": player_market_value,
        "player_club": player_club,
        "club_league": club_league,
        "player_club_league_level": player_club_league_level,
        "player_international_squad": player_international_squad,
        "player_birthplace": player_birthplace,
        "player_agent": player_agent,
        "player_height": player_height,
        "player_citizenship": player_citizenship,
        "player_position": player_position,
        "player_image_url": player_image_url,
        "player_further_information": player_further_information_list
    }

    return player_details

def get_player_club_details(player_id, player_name, headers):
    url = "https://www.transfermarkt.com/" + player_name + "/profil/spieler/" + str(player_id)
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    player_club = soup.select_one('span[class="data-header__club"]').text.strip()
    club_league = soup.select_one('span[class="data-header__league"]').text.strip()
    player_club_league_level = re.search("League level:\s*(.*)", soup.text).group(1)

    player_joined_date = re.search("Joined: (.*)", soup.text).group(1)
    player_contract_expiry = re.search("Contract expires: (.*)", soup.text).group(1)

    # Reveal the name of the club from the given id
    club_id = 0
    with open("club-ids-to-names.json", "r") as f:
        club_ids_to_names = json.load(f)
        for club in club_ids_to_names:
            if club["club_name"] == player_club:
                club_id = club["club_id"]

    player_club_details = {
        "player_club": player_club,
        "club_league": club_league,
        "player_club_league_level": player_club_league_level,
        "player_joined_date": player_joined_date,
        "player_contract_expiry": player_contract_expiry,
        "club_id": club_id
    }

    return player_club_details

def get_rumours(player_id, headers):
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

        rumours.append({
            "club": name,
            "competition": competition
        })

    return rumours