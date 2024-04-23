
# api things
from os import system

import requests
import sys


url = "http://192.168.137.1:8080/home?"
params = {"joke":"a joke"}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code)

system("python notes.py \"this is a joke\"")

# setters and getters 


