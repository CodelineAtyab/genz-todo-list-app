import requests
import json

"""
This program takes advantage of Google Matrix API, given two destinations,
it will calculate, distance, time, etc.
"""

origin = input("Enter origin: ")
end = input("Enter endpoint: ")


query_string_params = {"destinations": end,
                       "origins": origin,
                       "units": "metric",
                       "key": "AIzaSyC0PsPb31j531SYnJYLKzivuibohA20IbU"
                       }

response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=query_string_params)

print(f'Time to destination {response.json()["rows"][0]["elements"][0]["duration"]["text"]}')
