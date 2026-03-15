import pymongo
import os
# from dotenv import load_dotenv
import json

# load_dotenv()

# .env file
# host = os.getenv("MONGODB_HOST")
# database = os.getenv("MONGODB_DATABASE")
# user = os.getenv("MONGODB_USER")
# password = os.getenv("MONGODB_PASSWORD")

# os variables
host = os.environ.get("MONGODB_HOST")
database = os.environ.get("MONGODB_DATABASE")
user = os.environ.get("MONGODB_USER")
password = os.environ.get("MONGODB_PASSWORD")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

print(f"Host: {host}")
print(f"Database: {database}")
print(f"User: {user}")
print(f"Password: {password}")

print(myclient.list_database_names())

mydb = myclient["football-mercato"]

mycol = mydb["bundesliga-transfers-history-football-apis"]

with open("results.json", "r") as f:
    transfers = json.load(f)
    for transfer in transfers:
        x = mycol.insert_one(transfer)
        print(x)