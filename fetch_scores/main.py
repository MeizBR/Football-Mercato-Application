import requests

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

matches = []

def fetch_club_images(clubs_dictionary: dict, club_name: str) -> str:
    for club_key, club_info in clubs_dictionary.items():
        if club_info["short_name"].lower() == club_name.lower():
            logo_url = club_info["logo_page"]
            return logo_url
    return ""  # Return an empty string if the club is not found

response = requests.get(
    'https://live-football-api.com/api/v1/matches',
    params={'api_key': 'e380ec8493d7b09a56c3f2d24531b8e2ebda85fba51241a2a83587e53fffa4f8', 'date': '2026-11-22', 'lang': 'en'}
).json()

# Fetch Premier League matches and print the scores
for match in response['data']['matches']:
    if match["league"]["name"] == "Premier League" and match["league"]["country"] == "England":
        home = match['home']['name']
        home_score = match['home']['score']
        home_image = fetch_club_images(PREMIER_LEAGUE_CLUBS_2026_27, home)
        away = match['away']['name']
        away_score = match['away']['score']
        away_image = fetch_club_images(PREMIER_LEAGUE_CLUBS_2026_27, away)
        status = match['status']['status']
        display = match['status']['display']
        is_live = match['status']['is_live']
        state = match['status']['state']
        matches.append({
            "home": home,
            "home_score": home_score,
            "home_image": home_image,
            "away": away,
            "away_score": away_score,
            "away_image": away_image,
            "status": status,
            "display": display,
            "is_live": is_live,
            "state": state
        })
        # print(f"{home} {home_score} - {away_score} {away}")
        # print(f"Home Image: {home_image}")
        # print(f"Away Image: {away_image}")
        # print(f"Status: {status}")
        # print(f"Display: {display}")
        # print(f"Is Live: {is_live}")
        # print(f"State: {state}")
        # print("-" * 30)

print(matches)