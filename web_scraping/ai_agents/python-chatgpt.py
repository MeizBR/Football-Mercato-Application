from openai import OpenAI
from pydantic import BaseModel
from typing import List
import json
import os
from datetime import date

today = date.today().strftime("%B %d, %Y")

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

class NewsItem(BaseModel):
    id: str
    title: str
    player_name: str
    club_from: str
    club_to: str
    news_type: str
    source: str
    date: str
    reliability_score: int
    summary: str

class NewsList(BaseModel):
    news: List[NewsItem]

prompt = f"""
Generate the latest football transfer news as of {today}.

Only include recent and relevant updates.
Do not include outdated or old transfers.

Include:
- Rumours
- Near deals
- Official transfers
- Monitoring

Return at least 5 items.

Each item must include a date in format YYYY-MM-DD.

Output must follow this JSON schema:
{{
  "news": [
    {{
      "id": string,
      "title": string,
      "player_name": string,
      "club_from": string,
      "club_to": string,
      "news_type": "rumour | near_deal | official | monitoring",
      "source": string,
      "date": string,
      "reliability_score": number,
      "summary": string
    }}
  ]
}}

Rules:
- Return ONLY JSON
- No explanation
"""

response = client.responses.parse(
    model="gpt-5.4",
    tools=[{"type": "web_search"}],
    input=[
        {
            "role": "developer",
            "content": "You are a professional football journalist."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    text_format=NewsList
)

res = response.output_parsed

print(res)

with open("results_file.json", "w") as f:
    json.dump(res.model_dump(), f, indent=2)