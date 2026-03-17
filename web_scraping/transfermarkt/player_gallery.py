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

def get_player_gallery(player_id, headers):
    player_gallery_url = "https://tmapi-alpha.transfermarkt.technology/player/" + str(player_id) + "/gallery"

    player_gallery_response = requests.get(
        player_gallery_url,
        headers=headers
    ).json()

    value = {}
    values = []

    gallery_images = player_gallery_response["data"]["images"]

    for image in gallery_images:
        value = {
            "image_title": image["title"],
            "image_url": image["url"],
        }

        values.append(value)
        x = mycol.insert_one(value)
        logs.append(x.inserted_id)

    return values, logs

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    gallery_data, logs = get_player_gallery(headers)

    print("Transfer news table:\n")
    for item in gallery_data:
        print(item)

    print("\nLogs:\n")
    for log in logs:
        print(log)