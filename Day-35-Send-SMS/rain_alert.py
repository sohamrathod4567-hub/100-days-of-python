import requests
from twilio.rest import Client
api_key = "API key here"
account_sid = "Account Sid here"
auth_token = "Auth token here"

parameters = {
    "key":api_key,
    "q":"Surat",
    "api":"no"

}

response = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters)
response.raise_for_status()
response_json = response.json()
will_it_rain = response_json["current"]["chance_of_rain"]
print(will_it_rain)

if will_it_rain > 30:
    client = Client(account_sid , auth_token)
    message = client.messages \
        .create(
        # body= " It's Going to Rain Nigah",
        # from= "The Twilio Number",
        # to = "Your-number"

    )
    print("Bring the Umbrella nigah")
else:
    print("It's alright Nigah")

