import googlemaps, requests, json
from datetime import datetime

gmaps = googlemaps.Client(key="GOOGLEPLACES_KEY")

url="https://maps.googleapis.com/maps/api/place/textsearch/json?"

query = input('Search query: ')

r = requests.get(url + 'query=' + query +
                        '&key=' + api_key)


test_places= gmaps.text_search(
    "therapist",
    "textquery",
    fields= ["name", "formatted_address"],
    location_bias="ipbias",
    )
print(test_places)
