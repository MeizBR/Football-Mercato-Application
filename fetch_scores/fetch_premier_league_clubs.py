import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
import sys

current_dir = Path.cwd() / "web_scraping" / "transfermarkt"

sys.path.insert(0, str(current_dir))

from get_machine_headers import get_machine_headers

headers = get_machine_headers()

rumours_url = "https://www.premierleague.com/en/clubs"

rumours_url_response = requests.get(
    rumours_url,
    headers=headers
)

soup = BeautifulSoup(rumours_url_response.text, "html.parser")

# print(soup)

# for img in soup.select('img.club-badge__img'):
#     link = img.get("src", "")
#     print(link)

print(soup.select('img.club-badge__img'))

PREMIER_LEAGUE_CLUBS_2026_27 = {
    "arsenal": {
        "name": "Arsenal",
        "short_name": "Arsenal",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/3.svg"
    },
    "aston_villa": {
        "name": "Aston Villa",
        "short_name": "Aston Villa",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/7.svg"
    },
    "bournemouth": {
        "name": "AFC Bournemouth",
        "short_name": "Bournemouth",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/91.svg"
    },
    "brentford": {
        "name": "Brentford",
        "short_name": "Brentford",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/94.svg"
    },
    "brighton": {
        "name": "Brighton & Hove Albion",
        "short_name": "Brighton",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/36.svg"
    },
    "chelsea": {
        "name": "Chelsea",
        "short_name": "Chelsea",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/8.svg"
    },
    "coventry": {
        "name": "Coventry City",
        "short_name": "Coventry",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/9.svg"
    },
    "crystal_palace": {
        "name": "Crystal Palace",
        "short_name": "Crystal Palace",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/31.svg"
    },
    "everton": {
        "name": "Everton",
        "short_name": "Everton",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/11.svg"
    },
    "fulham": {
        "name": "Fulham",
        "short_name": "Fulham",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/54.svg"
    },
    "hull_city": {
        "name": "Hull City",
        "short_name": "Hull City",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/88.svg"
    },
    "ipswich_town": {
        "name": "Ipswich Town",
        "short_name": "Ipswich",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/40.svg"
    },
    "leeds_united": {
        "name": "Leeds United",
        "short_name": "Leeds United",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/2.svg"
    },
    "liverpool": {
        "name": "Liverpool",
        "short_name": "Liverpool",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/14.svg"
    },
    "manchester_city": {
        "name": "Manchester City",
        "short_name": "Man. City",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/43.svg"
    },
    "manchester_united": {
        "name": "Manchester United",
        "short_name": "Man. United",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/1.svg"
    },
    "newcastle_united": {
        "name": "Newcastle United",
        "short_name": "Newcastle",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/4.svg"
    },
    "nottingham_forest": {
        "name": "Nottingham Forest",
        "short_name": "Not. Forest",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/17.svg"
    },
    "sunderland": {
        "name": "Sunderland",
        "short_name": "Sunderland",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/56.svg"
    },
    "tottenham": {
        "name": "Tottenham Hotspur",
        "short_name": "Tottenham",
        "logo_page": "https://resources.premierleague.com/premierleague25/badges-alt/6.svg"
    }
}