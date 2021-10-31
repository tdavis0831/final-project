import googlemaps
from datetime import datetime
import os 


gmaps = googlemaps.Client(key=os.environ['GOOGLEPLACES_KEY'])





test_places= gmaps.find_place(
    "restaurant",
    "textquery",
    fields=["business_status", "geometry/location", "place_id", "name"],
    location_bias="point:90,90",
    )
print(test_places)
