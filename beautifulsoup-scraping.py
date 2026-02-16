from bs4 import BeautifulSoup
import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
}

url = "https://www.transfermarkt.com/castello-lukeba/profil/spieler/618472"
player_id = url.split('/')[-1]

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

player_name = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
player_number = soup.select_one('span[class="data-header__shirt-number"]').text.strip().replace('#', '')
player_club = soup.select_one('span[class="data-header__club"]').text.strip()
club_league = soup.select_one('span[class="data-header__league"]').text.strip()

# print (f"Player ID: {player_id}")
# print(f"Player Name: {player_name}")
# print(f"Player Number: {player_number}")
# print(f"Player Club: {player_club}")
# print(f"Club League: {club_league}")

# print("Current Rumours:")

# club_rumour = requests.get(
#         'https://www.transfermarkt.com/ceapi/currentRumors/player/618472/',
#         headers=headers
# ).json()

# rumors = club_rumour["rumors"]
# for rumor in rumors:
#     club = rumor["club"]
#     name = club["name"]
#     competition = club["competitionName"]

#     print(f"Club: {name}, Competition: {competition}")

# print("Player Career:")

player_career = requests.get(
        'https://tmapi-alpha.transfermarkt.technology/clubs?ids[]=1041&ids[]=23826&ids[]=12764&ids[]=7813&ids[]=69570',
        headers=headers
).json()

# player_history = soup.select_one('a[class="tm-player-transfer-history-grid__club-link"]').text.strip()
# player_history = soup.find_all('a')

# print(f"Player History: {player_history}")

# soup_1 = BeautifulSoup('<img src="https://img.a.transfermarkt.technology/portrait/header/618472-1713897532.jpg?lm=1" title="Castello Lukeba" alt="Castello Lukeba" class="data-header__profile-image" height="181" width="139">', "lxml")

# tag = soup_1.img
# print(tag['src'])

player_history = soup.select_one('ul[class="data-header__items"]').text.strip()
print(player_history)