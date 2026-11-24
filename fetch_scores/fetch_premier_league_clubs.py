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

