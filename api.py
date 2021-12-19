import requests
import json
from pprint import pprint
import server
import os
def get_therapist_info(city):
	
	textChoice = "Therapist"
	
	API_key = os.environ['YELP_API']
	client_id = 'Your Client ID'
	ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
	HEADERS = {'Authorization': f'Bearer {API_key}'}

	PARAMETERS = {
		'term' : textChoice,
		'limit' : 10,
		'location' : city,
		'radius' : 10000
	}

	response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
	data = response.json()


	provider_list=[]
	for place in data['businesses']:
		provider_dict={}
  
		
		provider_dict['name']=(place['name'])
		provider_dict['other']=( place['phone'])
		provider_dict['address']=(place['location']['display_address'])
		provider_list.append(provider_dict)

	return provider_list