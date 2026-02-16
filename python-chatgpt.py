import os
import requests
from datetime import date

api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

today = date.today().strftime("%Y-%m-%d")

prompt = f"""
You are a football transfer market journalist.

Task:
Generate the latest football transfer mercato updates for TODAY ({today}).

Rules:
- Provide EXACTLY 10 transfer news items.
- Mix official transfers, strong rumors, and close-to-sign deals.
- Focus on top European leagues (Premier League, La Liga, Serie A, Bundesliga, Ligue 1).
- Do NOT repeat the same player or club.
- Prioritize realistic and credible news.

Format EACH item exactly like this:

[TYPE] Player Name — From Club → To Club
Status: Official / Close / Rumor
Details: One short factual sentence.
Source: Trusted media or journalist

TYPE must be ONE of:
- OFFICIAL
- CLOSE
- RUMOR

Output rules:
- Number items from 1 to 10
- No emojis
- No commentary outside the list
"""

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "max_tokens": 500,
    "temperature": 0.6
}

response = requests.post(api_endpoint, headers=headers, json=data)

if response.status_code != 200:
    raise Exception(response.text)

print(response.json()["choices"][0]["message"]["content"])