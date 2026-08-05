import requests
from datetime import datetime

# Link : https://pixe.la/v1/users/soham9/graphs/graph1.html   From here we can access the graph
USERNAME = "soham9"
TOKEN = "123456789"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "BookReading",
    "unit": "Pages",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config , headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")


pixel_config = {
    "date": today,
    "quantity":"7"
}

pixel_update = {
    "quantity": "6"
}
pixel_update_endpoint = f"{pixel_endpoint}/{today}"

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

response = requests.put(url=pixel_update_endpoint, headers = headers, json = pixel_update )