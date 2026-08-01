import requests
api_key = ""

parameters = {
    "key":api_key,
    "q":"Surat",
    "api":"no"

}

response = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters)
response.raise_for_status()
response_json = response.json()
print(response_json["current"]["chance_of_rain"])

