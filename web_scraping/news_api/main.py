from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='')

# /v2/everything
all_articles = newsapi.get_everything(q='Fabrizio Romano', language='en', page_size=20)

response = []

for article in all_articles["articles"]:
    a = {
        "date": article["publishedAt"],
        "author": article["author"],
        "title": article["title"],
        "url": article["url"],
        "image": article["urlToImage"]
    }

    response.append(a)

print(response)