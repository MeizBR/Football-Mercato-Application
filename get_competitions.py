import requests
from bs4 import BeautifulSoup
import re
import get_machine_headers
import json

def get_element_occurences(s, e):
    i = 0
    for element in s:
        if element == e:
            i += 1
    return i

def split_string(s):
    r = ""
    for i in range(get_element_occurences(s, "-") + 1):
        r+= (s.split("-")[i]).capitalize() + " "
    return r.strip()

url = "https://www.transfermarkt.com/navigation/wettbewerbe"

headers = get_machine_headers.get_machine_headers()

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

competitions_names = set()
competitions_links = set()

competitions = []
links_list = []

def get_competitions():
    for link in soup.select("ul.tm-button-list li a"):
        href = link.get("href", "")
        
        competition_name = href.split("/")[1]
        competition_link = href

        competitions_names.add(competition_name)
        competitions_links.add(competition_link)

    for competition_name, competition_link in zip(competitions_names, competitions_links):
        competitions.append({
            "competition_name": split_string(competition_name),
            "competition_link": "https://www.transfermarkt.com" + competition_link
        })

    for competition in competitions:
        links_list.append(competition["competition_link"])

    return links_list

print(get_competitions())
with open("competitions.txt", "a") as f:
    for competition in competitions:
        f.write(split_string(competition["competition_name"]))
        f.write("\n")