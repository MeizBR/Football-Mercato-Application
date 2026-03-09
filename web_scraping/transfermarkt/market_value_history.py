import requests

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

    return values