import requests

url = "https://console.firebase.google.com/u/0/project/ai-agency-6d52c/database/ai-agency-6d52c-default-rtdb/data/~2F?utm_source=chatgpt.com/data.json"

data = {
    "income": 100000,
    "website": 5
}

r = requests.put(url, json=data)

print(r.text)
