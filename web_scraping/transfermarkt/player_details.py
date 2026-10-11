# Enhanced code (written by me, enhanced by AI)
from bs4 import BeautifulSoup
import re
import requests


# ---------------- SAFE HELPERS ---------------- #

def safe_select_text(soup, selector):
    el = soup.select_one(selector)
    return el.text.strip() if el else None


def safe_select_attr(soup, selector, attr):
    el = soup.select_one(selector)
    return el[attr] if el and el.has_attr(attr) else None


def safe_regex(pattern, text):
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else None

def safe_name(soup, selector):
    el = soup.select_one(selector)
    if not el:
        return None
    return el.text.split("\n")[-1].strip()


# ---------------- PLAYER DETAILS ---------------- #

def get_player_details(player_id, player_name, headers):

    url = f"https://www.transfermarkt.com/{player_name}/profil/spieler/{player_id}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("Request error:", e)
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    page_text = soup.text


    player_name = safe_name(
        soup,
        "h1.data-header__headline-wrapper"
    )

    player_number = safe_select_text(
        soup,
        'span.data-header__shirt-number'
    )

    if player_number:
        player_number = player_number.replace("#", "")

    player_market_value = safe_select_text(
        soup,
        'a.data-header__market-value-wrapper'
    )

    player_international_squad = safe_regex(
        r"Current international:.*?([A-Za-z].*?)\n",
        page_text
    )

    player_birthplace = safe_regex(
        r"Place of birth:.*?([A-Za-z].*?) ",
        page_text
    )

    player_agent = safe_regex(
        r"Agent:.*?([A-Za-z].*?)\n",
        page_text
    )

    player_height = safe_regex(
        r"Height:.*?([0-9].*?)\n",
        page_text
    )

    player_citizenship = safe_regex(
        r"Citizenship:.*?([A-Za-z].*?)\n",
        page_text
    )

    player_position = safe_regex(
        r"Position:.*?([A-Za-z].*?)\n",
        page_text
    )

    player_image_url = safe_select_attr(
        soup,
        "img.data-header__profile-image",
        "src"
    )

    further_info = safe_select_text(
        soup,
        "div.content"
    )

    if further_info:
        player_further_information_list = further_info.split(".")
    else:
        player_further_information_list = []


    player_details = {
        "player_name": player_name,
        "player_number": player_number,
        "player_market_value": player_market_value,
        "player_international_squad": player_international_squad,
        "player_birthplace": player_birthplace,
        "player_agent": player_agent,
        "player_height": player_height,
        "player_citizenship": player_citizenship,
        "player_position": player_position,
        "player_image_url": player_image_url,
        "player_further_information": player_further_information_list,
    }

    return player_details


# ---------------- CLUB DETAILS ---------------- #

def get_player_club_details(player_id, player_name, headers):

    url = f"https://www.transfermarkt.com/{player_name}/profil/spieler/{player_id}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("Request error:", e)
        return None

    soup = BeautifulSoup(response.content, "html.parser")
    page_text = soup.text

    player_club_id_0 = safe_select_attr(
        soup,
        "a.data-header__box__club-link img",
        "srcset"
    )

    h_index = player_club_id_0.find("h")
    x_index = player_club_id_0.find("1x")

    player_club_id = player_club_id_0[h_index:x_index-1]

    player_club = safe_select_text(
        soup,
        "span.data-header__club"
    )

    club_league = safe_select_text(
        soup,
        "span.data-header__league"
    )

    player_club_league_level_0 = safe_regex(
        r"League level:\s*(.*)",
        page_text
    )

    new_line_index = player_club_league_level_0.find("\n")
    player_club_league_level = player_club_league_level_0[:new_line_index].strip()

    player_joined_date_0 = safe_regex(
        r"Joined: (.*)",
        page_text
    )

    new_line_index_1 = player_joined_date_0.find("\n")
    player_joined_date = player_joined_date_0[:new_line_index_1].strip()

    player_contract_expiry_0 = safe_regex(
        r"Contract expires: (.*)",
        page_text
    )

    new_line_index_2 = player_contract_expiry_0.find("\n")
    player_contract_expiry = player_contract_expiry_0[:new_line_index_2].strip()

    return {
        "player_club": player_club,
        "club_id": player_club_id,
        "club_league": club_league,
        "player_club_league_level": player_club_league_level,
        "player_joined_date": player_joined_date,
        "player_contract_expiry": player_contract_expiry,
    }


# ---------------- RUMOURS ---------------- #

def get_rumours(player_id, headers):

    url = f"https://www.transfermarkt.com/ceapi/currentRumors/player/{player_id}/"

    try:
        data = requests.get(url, headers=headers, timeout=20).json()
    except Exception as e:
        print("Rumor error:", e)
        return []

    rumours = []

    for rumor in data.get("rumors", []):

        club = rumor.get("club", {})

        rumours.append({
            "club": club.get("name"),
            "competition": club.get("competitionName")
        })

    return rumours