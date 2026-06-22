import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("Scheme Name:", data["meta"]["scheme_name"])

df = pd.DataFrame(data["data"])

df.to_csv("data/raw/live_nav.csv", index=False)

print("Live NAV data saved successfully!")