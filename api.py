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

# def get_therapist_info():
# for place in data['businesses']:
 
	
# 	therapist_info = (place['phone'], place['name'], place['location']['display_address'])
	
	
# 	return (therapist_info)

def get_therapist_info():

	provider_list=[]
	for place in data['businesses']:
		provider_dict={}
  
		print("")
		provider_dict['name']=(place['name'])
		provider_dict['other']=( place['phone'], place['location']['display_address'])

		provider_list.append(provider_dict)
	print(provider_list)
	return provider_list
		




	# 	provider_list=[]
	
	# 	provider_list.append([(place['name'], place['phone'], place['location']['display_address'])])
	# return provider_list
	
# therapist_info = (place['phone'], place['name'], place['location']['display_address'])