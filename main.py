from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/players")
def get_players():
    return {
        "players": [
            {"name": "Player 1", "club": "Club A"},
            {"name": "Player 2", "club": "Club B"}
        ]
    }