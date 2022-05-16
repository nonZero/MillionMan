import sys

import requests

BASE_URL = "http://127.0.0.1:9361"

endpoint = f"{BASE_URL}/api/expense/"

if len(sys.argv) > 1:
    amount = float(sys.argv[1])
    title = " ".join(sys.argv[2:])
    r = requests.post(
        endpoint,
        {
            "title": title,
            "amount": amount,
            "user": 1,
            "category": 8,
        },
    )
    print(r.json())
    r.raise_for_status()

r = requests.get(
    endpoint,
    headers={
        # "Authorization": "Token 6b0f0d1ccd386d1582b97ebdc5de9571048c3673",
    },
)
r.raise_for_status()

data = r.json()
for e in data[:10]:
    print(f"#{e['id']}: ${e['amount']} {e['title']} {e['user']}")
