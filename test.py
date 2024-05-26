import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes":10,"views":45,"name":"first"},
#     {"likes":15,"views":86,"name":"second"},
#     {"likes":20,"views":416,"name":"third"}
# ]
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()

#  requests.patch(BASE + "video/1",{"views": 154})
#  requests.delete(BASE + "video/1")

response = requests.get(BASE + "video/1")
print(response.json())