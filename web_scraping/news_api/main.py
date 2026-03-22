from newsapi import NewsApiClient
import pymongo
import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get("MONGODB_HOST")
database = os.environ.get("MONGODB_DATABASE")
user = os.environ.get("MONGODB_USER")
password = os.environ.get("MONGODB_PASSWORD")
news_api_key = os.environ.get("NEWS_API_KEY")

myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{host}")

print(f"Host: {host}")
print(f"Database: {database}")
print(f"User: {user}")
print(f"Password: {password}")
print(f"News API key: {news_api_key}")

print(myclient.list_database_names())

mydb = myclient["football-mercato"]

mycol = mydb["news-api-results"]

def getResults(q, apiKey):
    mycol.delete_many({})
    time.sleep(2)

    logs = []

    # Init
    newsapi = NewsApiClient(api_key=apiKey)

    # /v2/everything
    all_articles = newsapi.get_everything(q=q, language='en', page_size=20)

    response = []

    for article in all_articles["articles"]:
        a = {
            "date": article["publishedAt"],
            "author": article["author"],
            "title": article["title"],
            "url": article["url"],
            "image": article["urlToImage"]
        }

        x = mycol.insert_one(a)
        logs.append(x.inserted_id)

        response.append(a)

    return response, logs

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python3 file.py <query>")
        sys.exit(1)

    q = sys.argv[1]

    news_api_data, logs = getResults(q, news_api_key)

    print("Transfer news table:\n")
    for item in news_api_data:
        print(item)

    print("\nLogs:\n")
    for log in logs:
        print(log)