import http.client
import json

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    "x-apisports-key": "6e0302c89decf6ca9128074a8e024f98"
}

params = {
    "league": "39",
    "season": "2024"
}

conn.request("GET", "/teams?league={league}&season={season}".format(**params), headers=headers)

res = conn.getresponse()
data = res.read()

data_json = json.loads(data.decode("utf-8"))

teams = []

for team in data_json["response"]:
    t = {
        "team": {
            "id": team["team"]["id"],
            "name": team["team"]["name"],
            "code": team["team"]["code"],
            "country": team["team"]["country"],
            "logo": team["team"]["logo"],
        },
        "stadium": {
            "id": team["venue"]["id"],
            "name": team["venue"]["name"],
            "address": team["venue"]["address"],
            "city": team["venue"]["city"],
            "capacity": team["venue"]["capacity"],
            "image": team["venue"]["image"],
        }
    }

    teams.append(t)

with open("Premier-League-Clubs-Football-API.json", "w", encoding="utf-8") as f:
    json.dump(teams, f, indent=2)

print(teams)