import requests

# Linux headers
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
}

player_id = 566799

def get_transfer_history(player_id, headers):
    transfer_history_url = "https://tmapi-alpha.transfermarkt.technology/transfer/history/player/" + str(player_id)

    transfer_history_response = requests.get(
        transfer_history_url,
        headers=headers
    ).json()

    value = {}
    values = []

    transfer_history_result = transfer_history_response["data"]["history"]["terminated"]

    for transfer in transfer_history_result:
        value = {
            "transfer_source": {
                "competition_id": transfer["transferSource"]["competitionId"],
                "country_id": transfer["transferSource"]["countryId"],
                "club_id": transfer["transferSource"]["clubId"],
            },
            "transfer_destination": {
                "competition_id": transfer["transferDestination"]["competitionId"],
                "country_id": transfer["transferDestination"]["countryId"],
                "club_id": transfer["transferDestination"]["clubId"],
            },
            "date": transfer["details"]["date"],
            "contract_until_date": transfer["details"]["contractUntilDate"],
            "season_id": transfer["details"]["seasonId"],
            "market_value": {
                "amount": transfer["details"]["marketValue"]["value"],
                "currency": transfer["details"]["marketValue"]["currency"],
            },
            "fee": {
                "amount": transfer.get("details", {}).get("fee", {}).get("value") or "not available",
                "currency": transfer.get("details", {}).get("fee", {}).get("currency") or "not available",
            }
        }

        values.append(value)

    return values

print(get_transfer_history(player_id, headers))