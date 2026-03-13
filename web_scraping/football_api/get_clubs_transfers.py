import http.client
import json
import datetime

# Get the current date and time object
current_datetime = datetime.datetime.now()

# Extract the year attribute and print it
previous_year = (current_datetime.year) - 1

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-apisports-key': ""
}

leagues = ["Premier-League", "Serie-A", "La-Liga", "Bundesliga", "Ligue-1"]

transfers = dict()

for league in leagues:
    with open(f"{league}-Clubs-Football-API.json", "r") as f:
        clubs = json.load(f)
        for club in clubs:
            conn.request("GET", f"/transfers?team={club['team']['id']}", headers=headers)
            res = conn.getresponse()
            data = res.read()
            data_json = json.loads(data.decode("utf-8"))

            club_transfers_details = []
            for transfer in data_json["response"]:
                t = {
                    "player": transfer["player"]["name"],
                    "transfers": transfer["transfers"]
                }
                club_transfers_details.append(t)

            transfers[club['team']['name']] = club_transfers_details

for club in transfers:
    filtered_transfers = []

    for transfer in transfers[club]:
        keep_transfer = True

        for t in transfer["transfers"]:
            if int(t["date"][:4]) < previous_year:
                keep_transfer = False
                break

        if keep_transfer:
            filtered_transfers.append(transfer)

    transfers[club] = filtered_transfers

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(filtered_transfers, f, indent=2)