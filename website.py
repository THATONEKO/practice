from datetime import date

import requests
BASE_URL = "https://api.carbonintensity.org.uk/intensity"

def fetch_last_half_hour() -> str:
    last_half_hour = requests.get(BASE_URL).json()["data"][0]
    return last_half_hour["intensity"]["actual"]

def fetch_from_to(start, end) -> list:
    return requests.get(f"{BASE_URL}/{start}/{end}").json()["data"]

if __name__ == "__main__":
    for entry in fetch_from_to(start=date(2023, 10, 1), end=date(2023, 10, 3)):
        print("From {from} to {to}: {intensity[actual]}".format(**entry))
