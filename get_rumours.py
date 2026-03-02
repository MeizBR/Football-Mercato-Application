import requests
from bs4 import BeautifulSoup
import re
import get_machine_headers
import json

headers = get_machine_headers.get_machine_headers()

rumours_url = "https://www.transfermarkt.com/rumourmill/detail/forum/154/page/1"

rumours_url_response = requests.get(
    rumours_url,
    headers=headers
)

soup = BeautifulSoup(rumours_url_response.text, "html.parser")

page_indexes = []

for link in soup.select('a.tm-pagination__link'):
    href = link.get("href", "")

    match = re.search(r"/page/(\d+)", href)
    if match:
        page_number = int(match.group(1))
        page_indexes.append(page_number)

max_page_index = max(page_indexes)
print(max_page_index)