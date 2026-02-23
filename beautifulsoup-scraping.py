from bs4 import BeautifulSoup
import re
import requests
import json

# Windows headers
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
# }

# Linux headers
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

player_id = 780136
player_name = "aleksandar-stankovic"
url = "https://www.transfermarkt.com/" + player_name + "/profil/spieler/" + str(player_id)

print(f"Fetching data for player Name: {player_name}, Player ID: {player_id} from URL: {url}")

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

player_name = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
player_number = soup.select_one('span[class="data-header__shirt-number"]').text.strip().replace('#', '')
player_club = soup.select_one('span[class="data-header__club"]').text.strip()
club_league = soup.select_one('span[class="data-header__league"]').text.strip()
player_international_squad = re.search("Current international:.*?([A-z].*?)\n", soup.text, re.DOTALL).group(1).strip()

print (f"Player ID: {player_id}")
print(f"Player Name: {player_name}")
print(f"Player Number: {player_number}")
print(f"Player Club: {player_club}")
print(f"Club League: {club_league}")
print(f"Player International Squad: {player_international_squad}")


print("Current Rumours:")

club_rumour_url = "https://www.transfermarkt.com/ceapi/currentRumors/player/" + str(player_id) + "/"

club_rumour = requests.get(
        club_rumour_url,
        headers=headers
).json()

rumors = club_rumour["rumors"]
for rumor in rumors:
    club = rumor["club"]
    name = club["name"]
    competition = club["competitionName"]

    print(f"Club: {name}, Competition: {competition}")


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