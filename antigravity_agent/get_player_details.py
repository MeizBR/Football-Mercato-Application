import requests

url = "https://api.sportdb.dev/api/flashscore/"
response = requests.get(url)

# Check HTTP Status Code
if response.status_code == 200:
    data = response.json()  # Automatically parses JSON response into a Python dict
    print("Data received:", data)
else:
    print(f"Request failed with status code: {response.status_code}")