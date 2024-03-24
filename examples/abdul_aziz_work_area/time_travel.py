import requests


def travel_time_estimator(origin, destination):
    """
    :param origin: the start point
    :param destination: the endpoint
    :return: the time will take to travel from the origin to the destination that were
    taken as input from the user
    """
    string_params = {
        "destinations": destination,
        "origins": origin,
        "key": "type your private key",
        "units": "metric"
    }

    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=string_params)
    print("The time taken to travel from", origin, "to", destination, "is", response.json()["rows"][0]["elements"][0]["duration"]["text"], ".")


origins = input("Enter the desired starting point: ")
destinations = input("Enter the desired destination: ")
(travel_time_estimator(origins, destinations))
