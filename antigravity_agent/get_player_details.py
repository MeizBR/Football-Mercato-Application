import requests

headers = {
    "X-API-Key": "7ygqBbBFuXBQxQIR8uw7RdycfIFvbbeuowJU5xZx"
}

url = "https://api.sportdb.dev/api/flashscore/football/england:198/premier-league:dYlOSQOD/2026-2027/results?page=1"
response = requests.get(url, headers=headers)

# Check HTTP Status Code
if response.status_code == 200:
    data = response.json()
    print("Data received:", data)
else:
    print(f"Request failed with status code: {response.status_code}")