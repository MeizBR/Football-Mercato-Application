import requests
from bs4 import BeautifulSoup
import re
import get_machine_headers
import get_competitions
import json

headers = get_machine_headers.get_machine_headers()

for competition in get_competitions.get_competitions():

    clubs = []
    unique_set = set()
    # t = []

    with open(f"{competition["name"]}-list-of-clubs.json", "w") as f:
        f.write("[\n")

    response = requests.get(competition["link"], headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # for i in soup.select("td[class='rechts hauptlink'] span"):
    #     title = i.get("title", "")
    #     t.append(int(title[14:len(title) - 6]))

    for link in soup.select("td.hauptlink a"):
        href = link.get("href", "")

        club_name_url = "https://www.transfermarkt.com" + href
        
        match = re.search(r"/verein/(\d+)", href)
        if match:
            club_id = int(match.group(1))
            club_name = link.text.strip()

            club_object = {
                "club_id": club_id,
                "club_name_url": club_name_url,
                "club_name": club_name
            }
            print(club_object)

            clubs.append(club_object)
        else:
            continue

    clubs = clubs[:competition["clubs"]]

    with open(f"{competition["name"]}-list-of-clubs.json", "a") as f:
        for club in clubs:
            f.write(json.dumps(club) + ",\n")

    with open(f"{competition["name"]}-list-of-clubs.json", "a") as f:
        f.write("]")