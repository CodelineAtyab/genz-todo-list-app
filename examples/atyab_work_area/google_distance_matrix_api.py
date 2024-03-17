import requests

query_string_params = {
    "destinations": "Oman avenues mall| Muscat",
    "origins": "Mall of Oman| Muscat",
    "alternatives": False,
    "units": "metric",
    "key": ""
}

response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=query_string_params)
print(response.json())
print(f'It will take {response.json()["rows"][0]["elements"][0]["duration"]["text"]}')
print(f'Distance is {response.json()["rows"][0]["elements"][0]["distance"]["text"]}')