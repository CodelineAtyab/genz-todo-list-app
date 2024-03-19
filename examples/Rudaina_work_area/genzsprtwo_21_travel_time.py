import requests

"""

origin: user input of origin place
destination: user input of distination
return: estimated travel time between the 2 destnatiosn
"""
def get_distance_and_duration(origin, destination):
    params = {
        'origins': origin,
        'destinations': destination,
        'key': "Enter API KEY HERE",
        'units': 'metric' 
    }

    try:
        response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?", params=params)
        data = response.json()

        if data['status'] == 'OK':
            for row in data['rows']:
                for element in row['elements']:
                    distance_text = element['distance']['text']
                    duration_text = element['duration']['text']
                    return distance_text, duration_text
        else:
            raise Exception(f"Error: {data['status']} - {data.get('error_message', '')}")

    except requests.RequestException as error:
        raise Exception(f"Error: Request failed -> {error}")

    except KeyError as e:
        raise Exception(f"Error: Invalid response format -> {error}")


"""
Ask the user to input an origin and a destination 
Print the estimated travel time between them from the returned distance and duration  
"""
print("Example of inputs:")
print("-----------------------------------------")
print(" origin = Oman Avenues Mall, Muscat, Oman\n destination = Muscat City Centre, Muscat, Oman ")
print("-----------------------------------------")
origin = input("Enter Origin: ")
destination = input("Enter Distination: ")
distance, duration = get_distance_and_duration(origin, destination)
print(f"Distance: {distance}, Duration: {duration}")
