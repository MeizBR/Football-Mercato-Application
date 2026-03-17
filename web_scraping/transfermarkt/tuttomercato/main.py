from bs4 import BeautifulSoup
import requests
import pymongo
import os

host = os.environ.get("MONGODB_HOST")
database = os.environ.get("MONGODB_DATABASE")
user = os.environ.get("MONGODB_USER")
password = os.environ.get("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

mydb = myclient["football-mercato"]

mycol = mydb["tuttomercato-news"]

def get_transfers_tuttomercato(headers):
    url = "https://www.transfermarketweb.com/transfers/"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    transfer_news_table = []

    details = []
    dates = []

    logs = []

    for content in soup.select("div.list ul li a"):
        for c in content.contents:
            details.append(c)

    for content in soup.select("div.list ul li span[class='small date']"):
        for c in content.contents:
            dates.append(c)

    for detail, date in zip(details, dates):
        d = {
                "date": date,
                "detail": detail
            }
        transfer_news_table.append(d)
        x = mycol.insert_one(d)
        logs.append(x.inserted_id)

    return transfer_news_table, logs

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    transfer_data, logs = get_transfers_tuttomercato(headers)

    print("Transfer news table:\n")
    for item in transfer_data:
        print(item)

    print("\nLogs:\n")
    for log in logs:
        print(log)