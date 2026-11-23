import requests

response = requests.get(
    'https://live-football-api.com/api/v1/matches',
    params={'api_key': 'e380ec8493d7b09a56c3f2d24531b8e2ebda85fba51241a2a83587e53fffa4f8', 'date': '2026-11-23', 'lang': 'en'}
).json()

# Fetch Premier League matches and print the scores
for match in response['data']['matches']:
    if match["league"]["name"] == "Premier League" and match["league"]["country"] == "England":
        home = match['home']['name']
        away = match['away']['name']
        home_score = match['home']['score']
        away_score = match['away']['score']
        status = match['status']['status']
        display = match['status']['display']
        is_live = match['status']['is_live']
        state = match['status']['state']
        print(f"{home} {home_score} - {away_score} {away}")
        print(f"Status: {status}")
        print(f"Display: {display}")
        print(f"Is Live: {is_live}")
        print(f"State: {state}")
        print("-" * 30)