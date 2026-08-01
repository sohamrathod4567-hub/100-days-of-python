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
will_it_rain = response_json["current"]["chance_of_rain"]

if will_it_rain > 30:
    print("Bring the Umbrella nigah")
else:
    print("It's alright Nigah")

