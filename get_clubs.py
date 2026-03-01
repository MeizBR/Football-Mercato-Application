import requests
from bs4 import BeautifulSoup
import re
import get_machine_headers
import get_competitions
import json

headers = get_machine_headers.get_machine_headers()

clubs = []
unique_set = set()

with open("club-ids-to-names.json", "w") as f:
    f.write("[\n")

for competition in get_competitions.get_competitions():

    response = requests.get(competition, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.select("td.hauptlink a"):
        href = link.get("href", "")
        
        match = re.search(r"/verein/(\d+)", href)
        if match:
            club_id = int(match.group(1))
            club_name = link.text.strip()

            club_object = {
                "club_id": club_id,
                "club_name": club_name
            }

            clubs.append(club_object)

            if club_id not in unique_set:
                with open("club-ids-to-names.json", "a") as f:
                    f.write(json.dumps(club_object) + ",\n")
                unique_set.add(club_id)
            else:
                continue
        else:
            continue

with open("club-ids-to-names.json", "a") as f:
    f.write("]")