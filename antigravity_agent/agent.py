from google import genai
import os
import requests
import tarfile
import shutil
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

today = date.today()

MAX_TOKENS = 6000

team_name = "Player_stats"

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
#     input = f"""
# System / Role Directive:
# You are the Manager of {team_name} Football Club in September 2026. Maintain a confident, professional managerial tone in your opening and closing remarks.

# Task:
# 1. Search and retrieve all official {team_name} transfer arrivals for the Summer 2026 Transfer Window.
# 2. Generate a complete, standalone HTML file (including `<!DOCTYPE html>`, `<head>`, `<style>`, and `<body>` tags) containing a review of these transfers.

# Requirements:

# 1. Persona & Manager Statement:
#    - Address the fans/interviewer directly as the {team_name} manager.
#    - Summarize the strategic vision behind our Summer 2026 transfer window.

# 2. Web Search & Data Retrieval:
#    - Use your search tools to find all official major transfers completed by {team_name} during the Summer 2026 window.
#    - Gather details for each signing: player name, age, position, nationality, previous club, transfer fee, and photo URL.

# 3. HTML File Generation & Formatting:
#    - Structure the output as a valid, self-contained HTML document.
#    - Display the player transfers inside a clean, responsive HTML `<table>`.
#    - Include modern CSS styling within a `<style>` block in the head (e.g., {team_name} navy `#034694` headers, alternating row colors `#f8f9fa`, rounded borders, responsive padding).

# 4. Required Table Columns:
#    - Player Photo: An `<img>` tag referencing a direct image/avatar URL of the player.
#    - Player Name & Age
#    - Position & Nationality
#    - Previous Club
#    - Transfer Fee (in £)
#    - Profile & Tactical Fit: A brief description detailing the player's key attributes, tactical role, and why we signed them.

# Output Deliverable:
# - Output the complete, executable HTML code so it can be saved directly into a `.html` file called {team_name}_summer_2026_transfers.html.
# """,
    input= f"""
    Run a comprehensive scan on current football transfer news and rumors for today {today}. Generate a structured markdown report covering top major movements with the following breakdown for each deal:

1. Deal Status & Terms: Player, Selling Club, Buying Club, Fee Structure (base + add-ons), Contract Details, and Source Credibility/Tier.
2. Player Analysis: Tactical profile, primary strengths, statistical highlights, and suitablity for the buying club's system.
3. Selling Club Perspective: Financial/squad context for letting the player leave and replacement status.
4. Buying Club Perspective: Role in squad, immediate tactical impact, and squad depth shift.

Output the result as a cleanly formatted markdown file in the root workspace named `transfer_analysis_report.md`.
""",
    environment="remote",
    # agent_config={
    #     "type": "antigravity",
    #     "max_total_tokens": MAX_TOKENS
    # }
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print("Status:", interaction.status)
print("Usage:", interaction.usage)
print(f"Output\n: {interaction.output_text}")


target_file_name = f"{team_name}_summer_2026_transfers.html"

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]
# api_key = os.getenv("MONGODB_HOST")

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

if response.status_code == 200:
    tar_filename = "snapshot.tar"
    with open(tar_filename, "wb") as f:
        f.write(response.content)
    print("Download complete.")

    # 2. Extract snapshot contents
    extract_dir = Path("extracted_snapshot")
    with tarfile.open(tar_filename) as tar:
        tar.extractall(path=extract_dir)
    print(f"Extracted snapshot into './{extract_dir}'")

    # 3. Locate the target HTML file inside the extracted tree
    matching_files = list(extract_dir.rglob(f"*{target_file_name}*"))

    if matching_files:
        source_path = matching_files[0]
        destination_path = Path(target_file_name)
        
        # Copy to local directory
        shutil.copy(source_path, destination_path)
        print(f"\n Success! Saved file to: {destination_path.resolve()}")
    else:
        print(f"\n⚠️ Could not find '{target_file_name}' inside the snapshot.")
        print("List of files found in environment snapshot:")
        for path in extract_dir.rglob("*"):
            if path.is_file():
                print(f" - {path.relative_to(extract_dir)}")
else:
    print(f"❌ Failed to download snapshot. HTTP Status: {response.status_code}")
    print(response.text)