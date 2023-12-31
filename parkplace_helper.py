import requests
from geographiclib.geodesic import Geodesic

PARKSPACE_URL = "https://data.sbb.ch/api/explore/v2.1/catalog/datasets/mobilitat/records?select=bezeichnung_offiziell%2Cgeopos&where=parkrail_anzahl%20%3E%200&limit=100"

N_SPOTS = 1000
cached_parkings = None

def get_all_available_parkings():
    global cached_parkings
    if cached_parkings is None:
        cached_parkings = []
        for i in range(int(N_SPOTS / 100)):
            new_ones = requests.get(PARKSPACE_URL + f"&offset={i*100}").json()["results"]
            for x in new_ones:
                if not any(x['bezeichnung_offiziell'] == y['bezeichnung_offiziell'] for y in cached_parkings):
                    cached_parkings.append(x)
            cached_parkings
    return cached_parkings

def closest_parkings(lat, lon, count):
    geod = Geodesic.WGS84 
    parkings = get_all_available_parkings()
    parkings.sort(key = lambda x: geod.Inverse(lat,lon, x["geopos"]["lat"], x["geopos"]["lon"])["s12"])
    parking = parkings[:count]
    parkings = [{"name": x["bezeichnung_offiziell"], "lat":x["geopos"]["lat"], "lon":x["geopos"]["lon"]} for x in parking]
    return parkings

get_all_available_parkings()
# print(closest_parkings(46.5203, 6.566, 10))