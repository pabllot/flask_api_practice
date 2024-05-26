import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "video/125", {"likes":10,"views":46,"name":"first"})
# print(response.json())
# input()
response = requests.get(BASE + "video/12775")
print(response.json())