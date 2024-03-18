import requests

"""
This program calculates the distance and time
required to reach from an origin to a destination
"""

def distance_and_duration(origin, destination):
    input_params = {
                     "origins": origin,
                     "destinations": destination,
                     "key": "Enter private key",
                     "units": "metric"
                  }
    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=input_params)

    print(f"\nThe time to destination is {response.json()["rows"][0]["elements"][0]["duration"]["text"]}.\nThe distance to destination is {response.json()["rows"][0]["elements"][0]["distance"]["text"]}.")


origin = input("Please enter the origin: ")
destination = input("Please enter the destination: ")
distance_and_duration(origin, destination)