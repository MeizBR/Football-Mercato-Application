from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='c82390888dbb4513a8b7a3ea3fce1306')

# /v2/everything
all_articles = newsapi.get_everything(q='Fabrizio Romano',
                                          language='en',
                                          page_size=20)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

print(sources)