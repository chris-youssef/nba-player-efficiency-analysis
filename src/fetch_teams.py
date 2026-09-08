import os
import requests
import pandas as pd

API_KEY = os.getenv("BALLDONTLIE_API_KEY")  # we'll set this in terminal
if not API_KEY:
    raise SystemExit("Missing BALLDONTLIE_API_KEY. Set it in your terminal first.")

url = "https://api.balldontlie.io/v1/teams"
headers = {"Authorization": API_KEY}

r = requests.get(url, headers=headers, timeout=30)
r.raise_for_status()

data = r.json()["data"]
df = pd.DataFrame(data)

df.to_csv("data/teams.csv", index=False)
print("Saved data/teams.csv")
print(df.head())