from bs4 import BeautifulSoup
import requests

def get_transfers_tuttomercato(headers):
    url = "https://www.transfermarketweb.com/transfers/"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    transfer_news_table = []

    details = []
    dates = []

    for content in soup.select("div.list ul li a"):
        for c in content.contents:
            details.append(c)

    for content in soup.select("div.list ul li span[class='small date']"):
        for c in content.contents:
            dates.append(c)

    for detail, date in zip(details, dates):
        transfer_news_table.append(
            {
                "date": date,
                "detail": detail
            }
        )

    return transfer_news_table