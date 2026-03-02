import pymongo
import os
from dotenv import load_dotenv
import json

load_dotenv()

host = os.getenv("MONGODB_HOST")
database = os.getenv("MONGODB_DATABASE")
user = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

print(f"Host: {host}")
print(f"Database: {database}")
print(f"User: {user}")
print(f"Password: {password}")

print(myclient.list_database_names())

mydb = myclient["football-mercato"]

mycol = mydb["clubs"]

with open("club-ids-to-names.json", "r") as f:
    club_ids_to_names = json.load(f)
    for club in club_ids_to_names:
        x = mycol.insert_one(club)
        print(x)