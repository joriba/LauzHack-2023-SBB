import requests
from geographiclib.geodesic import Geodesic

PARKSPACE_URL = "https://data.sbb.ch/api/explore/v2.1/catalog/datasets/mobilitat/records?select=bezeichnung_offiziell%2Cgeopos&where=parkrail_anzahl%20%3E%200&limit=-1"

def get_all_available_parkings():
    return requests.get(PARKSPACE_URL).json()["results"]

def closest_parkings(lat, lon, count):
    geod = Geodesic.WGS84 
    parkings = get_all_available_parkings()
    parkings.sort(key = lambda x: geod.Inverse(lat,lon, x["geopos"]["lat"], x["geopos"]["lon"])["s12"])
    parking = parkings[:count]
    parkings = [{"name": x["bezeichnung_offiziell"], "lat":x["geopos"]["lat"], "lon":x["geopos"]["lon"]} for x in parking]
    return parkings

# print(closest_parkings(46.5203, 6.566, 10))