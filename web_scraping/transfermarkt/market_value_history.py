import requests
import pymongo
import os

host = os.environ.get("MONGODB_HOST")
database = os.environ.get("MONGODB_DATABASE")
user = os.environ.get("MONGODB_USER")
password = os.environ.get("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

mydb = myclient["football-mercato"]

mycol = mydb["transfermarkt-market-value-history-news"]

logs = []

def fetch_market_value_history(player_id, headers):
    market_value_url = "https://tmapi-alpha.transfermarkt.technology/player/" + str(player_id) + "/market-value-history"

    market_value = requests.get(
            market_value_url,
            headers=headers
    ).json()

    value = {}
    values = []
    marketValue = market_value["data"]["history"]

    for i in range(len(marketValue)):
        value = {
            "amount": marketValue[i]["marketValue"]["value"],
            "currency": marketValue[i]["marketValue"]["currency"],
            "date": marketValue[i]["marketValue"]["determined"],
        }
        values.append(value)
        x = mycol.insert_one(value)
        logs.append(x.inserted_id)

    return values, logs

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    market_value_history_data, logs = fetch_market_value_history(headers)

    print("Transfer news table:\n")
    for item in market_value_history_data:
        print(item)

    print("\nLogs:\n")
    for log in logs:
        print(log)