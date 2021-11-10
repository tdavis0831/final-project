import requests
import json
from pprint import pprint

myCity = input("What is your city? ")
FoodChoice = "Therapist"

API_key = 'Your API Key'
client_id = 'Your Client ID'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'Bearer'
}

PARAMETERS = {
	'term' : FoodChoice,
	'limit' : 10,
	'location' : myCity,
	'radius' : 10000
}

response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
data = response.json()


for place in data['businesses']:
 
	print("")
	print(place['name'])
	print(place['location']['display_address'])
