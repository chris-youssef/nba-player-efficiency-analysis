import os
import requests
import pandas as pd

API_KEY = os.getenv("BALLDONTLIE_API_KEY")
if not API_KEY:
    raise SystemExit("Missing BALLDONTLIE_API_KEY. Set it in terminal first.")

BASE = "https://api.balldontlie.io/v1"
HEADERS = {"Authorization": API_KEY}

def search_players(query: str, per_page: int = 50) -> pd.DataFrame:
    params = {"search": query, "per_page": per_page}
    r = requests.get(f"{BASE}/players", headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return pd.DataFrame(r.json().get("data", []))

if __name__ == "__main__":
    query = "lebron"   # change this to whoever you want
    df = search_players(query)

    if df.empty:
        print(f"No results for: {query}")
    else:
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/players_search.csv", index=False)
        print("Saved data/players_search.csv")
        print(df[["id", "first_name", "last_name"]].head(20))
