import requests

# This feature will get the estimated time and distance between two locations

origin = input('Enter starting point: ')
end = input('Enter the destination: ')

param = {"destinations": end,
                       "origins": origin,
                       "units": "metric",
                       "key": "AIzaSyC0PsPb31j531SYnJYLKzivuibohA20IbU"
                       }

response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params = param)
res_dict = response.json()
print(f"The distance is {res_dict['rows'][0]['elements'][0]['distance']['text']} and the estimated time is {res_dict['rows'][0]['elements'][0]['duration']['text']}")

