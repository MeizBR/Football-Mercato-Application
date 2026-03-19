import requests
from bs4 import BeautifulSoup
import get_machine_headers

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

x = [
    {
        "name": "premier-league",
        "link": "https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1",
        "clubs": 20
    },
    {
        "name": "laliga",
        "link": "https://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1",
        "clubs": 20
    },
    {
        "name": "serie-a",
        "link": "https://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1",
        "clubs": 20
    },
    {
        "name": "bundesliga",
        "link": "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1",
        "clubs": 18
    },
    {
        "name": "ligue-1",
        "link": "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1",
        "clubs": 18
    },
    {
        "name": "liga-nos",
        "link": "https://www.transfermarkt.com/liga-nos/startseite/wettbewerb/PO1",
        "clubs": 18
    },
    {
        "name": "eredivisie",
        "link": "https://www.transfermarkt.com/eredivisie/startseite/wettbewerb/NL1",
        "clubs": 18
    },
    {
        "name": "jupiler-pro-league",
        "link": "https://www.transfermarkt.com/jupiler-pro-league/startseite/wettbewerb/BE1",
        "clubs": 16
    },
    {
        "name": "super-lig",
        "link": "https://www.transfermarkt.com/super-lig/startseite/wettbewerb/TR1",
        "clubs": 20
    },
    {
        "name": "eliteserien",
        "link": "https://www.transfermarkt.com/eliteserien/startseite/wettbewerb/NO1",
        "clubs": 16
    },
    {
        "name": "allsvenskan",
        "link": "https://www.transfermarkt.com/allsvenskan/startseite/wettbewerb/SE1",
        "clubs": 16
    },
    {
        "name": "super-league",
        "link": "https://www.transfermarkt.com/super-league/startseite/wettbewerb/C1",
        "clubs": 16
    },
    {
        "name": "super-liga",
        "link": "https://www.transfermarkt.com/superligaen/startseite/wettbewerb/DK1",
        "clubs": 12
    }
]

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

    # return links_list
    return x

# print(get_competitions())
# with open("competitions.txt", "a") as f:
#     for competition in competitions:
#         f.write(split_string(competition["competition_name"]))
#         f.write("\n")