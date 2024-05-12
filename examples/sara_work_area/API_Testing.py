import requests

response = requests.get(url="http://192.168.137.1:8080/home", params={'joke': 'Why did the programmer quit her job? Because she didn’t get arrays'})

print(response.text)
