import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GMAPS_API_KEY")
BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"
gmaps = googlemaps.Client(key=API_KEY)

BASE_PARAMS = {
    "units": "metric",
    "key": API_KEY,
}

def get_closest_by_car(origin, destinatinons: list):
    return gmaps.distance_matrix([origin], destinatinons)

def geocode(origin: str):
    return gmaps.geocode(origin)

def get_travel_time_by_car(origin, destination):
    return gmaps.distance_matrix([origin], [destination])["rows"][0]["elements"][0]