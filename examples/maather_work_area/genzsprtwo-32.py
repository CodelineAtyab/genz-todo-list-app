import requests
def travel_time_estimator(origin, destination):

    params = {
        "destinations": destination,
        "origins": origin,
        "key": "AIzaSyC0PsPb31j531SYnJYLKzivuibohA20IbU",
        "units": "metric"
    }

    try:
        response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?", params)
        data = response.json()
        print("The time it takes to travel from ", origin, " to ", destination, " is ", response.json()["rows"][0]["elements"][0]["duration"]["text"], ".")
        print(data)
    except requests.exceptions.RequestException as e:
        print("There was a problem with the request.")
    except KeyError:
        print("There was a problem processing the response data.")
    except Exception as e:
        print("An unexpected error occurred.")

        


origin = input("Enter the desired starting point: ")
destination = input("Enter the desired destination: ")
(travel_time_estimator(origin, destination))