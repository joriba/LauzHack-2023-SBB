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

def get_closest_by_car(origin, destinatinons: list[str]):
    return gmaps.distance_matrix([origin], destinatinons)

def geolocate(origin: str):
    return gmaps.geolocate(origin)