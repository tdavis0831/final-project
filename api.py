import googlemaps
from datetime import datetime
import os 

  
# importing required modules 
import requests, json 

api_key = os.environ['GOOGLEPLACES_KEY']
  
# url variable store url 
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
  
#  string on which to search 
query = "therapist"
  
# get method of requests module 
# return response object 
r = requests.get(url + 'query=' + query +
                        '&key=' + api_key) 
  
# json method of response object convert 
#  json format data into python format data 
x = r.json() 
  
y = x['results'] 
  

for i in range(len(y)): 
    list1 = []
    list2= []
    # Print value corresponding to the 
    # 'name' key at the index of y 
    list1.append(y[i]['name'])
    print(list1)

    list2.append(y[i]['formatted_address'])
    print(list2)
    # print(y[i]['formatted_address'])


    
# import requests

# url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name%2Crating%2Cformatted_phone_number&key={api_key}"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)






# test_places= gmaps.find_place(
#     "restaurant",
#     "textquery",
#     fields=["business_status", "geometry/location", "place_id", "name"],
#     location_bias="point:90,90",
#     )
# print(test_places)