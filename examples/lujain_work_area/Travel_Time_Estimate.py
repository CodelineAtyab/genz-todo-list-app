import requests

def distance_and_duration(origin, destination, key):
    input_params = {
        "origins": origin,
        "destinations": destination,
        "key": key,
        "units": "metric"
    }
    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=input_params)
    
    data = response.json()  
    
    if "rows" in data and len(data["rows"]) > 0:
        elements = data["rows"][0]["elements"]
        if len(elements) > 0:
            duration_text = elements[0]["duration"]["text"]
            distance_text = elements[0]["distance"]["text"]
            print(f"\nThe time to destination is {duration_text}.")
            print(f"The distance to destination is {distance_text}.")
        else:
            print("No data available.")
    else:
        print("No data available.")

def main():
    origin = input("The Starting Location: ")
    destination = input("Destination: ")
    api_key = input("Please enter your Google Maps API key: ")
    distance_and_duration(origin, destination, api_key)

main()
