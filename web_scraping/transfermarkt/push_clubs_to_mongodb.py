import json
import pymongo
import os

host = os.environ.get("MONGODB_HOST")
database = os.environ.get("MONGODB_DATABASE")
user = os.environ.get("MONGODB_USER")
password = os.environ.get("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

mydb = myclient["football-mercato"]

leagues_list = [
    "allsvenskan",
    "bundesliga",
    "eliteserien",
    "eredivisie",
    "jupiler-pro-league",
    "laliga",
    "liga-nos",
    "ligue-1",
    "premier-league",
    "serie-a",
    "super-league",
    "super-lig",
    "superliga"
]

for league in leagues_list:
    file_name = league  + "-list-of-clubs.json"
    collection_name = league + "-clubs-list"

    mycol = mydb[collection_name]

    with open(file_name, "r",  encoding="utf-8") as f:
        data = json.load(f)
        x = mycol.insert_many(data)
        print(x)