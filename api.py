import requests
import json
from pprint import pprint
import server
def get_therapist_info(city):
	
	FoodChoice = "Therapist"

	API_key = 'Your API Key'
	client_id = 'Your Client ID'
	ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
	HEADERS = {'Authorization': 'Bearer'}

	PARAMETERS = {
		'term' : FoodChoice,
		'limit' : 10,
		'location' : city,
		'radius' : 10000
	}

	response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
	data = response.json(


	provider_list=[]
	for place in data['businesses']:
		provider_dict={}
  
		print("")
		provider_dict['name']=(place['name'])
		provider_dict['other']=( place['phone'])
		provider_dict['address']=(place['location']['display_address'])
		provider_list.append(provider_dict)
	print(provider_list)
	return provider_list