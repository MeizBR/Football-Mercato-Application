# pip install requests
import requests
from bs4 import BeautifulSoup
import requests
import json

player_id = 780136
player_name = "aleksandar-stankovic"
url = "https://www.transfermarkt.com/" + player_name + "/profil/spieler/" + str(player_id)
apikey = '3b0cfa6d1a8c2ea464dcc9c3012519e19e103469'
params = {
    'url': url,
    'apikey': apikey,
}
response = requests.get('https://api.zenrows.com/v1/', params=params)

soup = BeautifulSoup(response.content, "html.parser")

player_name = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
player_number = soup.select_one('span[class="data-header__shirt-number"]').text.strip().replace('#', '')
player_club = soup.select_one('span[class="data-header__club"]').text.strip()
club_league = soup.select_one('span[class="data-header__league"]').text.strip()

print (f"Player ID: {player_id}")
print(f"Player Name: {player_name}")
print(f"Player Number: {player_number}")
print(f"Player Club: {player_club}")
print(f"Club League: {club_league}")