import googlemaps
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GMAPS_API_KEY")
BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"
#   ?destinations=<addresses, separated by |>
#   &origins=<starting point>
#   &units=metric
#   &key=AIzaSyC4BLR0fxjI9NaKTUBG6V2PcZYEK32GPlo

BASE_PARAMS = {
    "units": "metric",
    "key": API_KEY,
}

def get_closest_by_car(origin, destinatinons: list[str]):
    gmaps = googlemaps.Client(key=API_KEY)
    return gmaps.distance_matrix([origin], destinatinons)