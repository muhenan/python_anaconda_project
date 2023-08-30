import requests

if True:
    print("Hello")

response = requests.get("https://www.google.com")

if response.status_code == 200:
    print("Get succeed")
    print("Google homepage content length:", len(response.text))
else:
    print("Failed to fetch Google homepage. Status code:", response.status_code)

