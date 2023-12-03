import requests
from requests_oauth2client import OAuth2Client, OAuth2ClientCredentialsAuth
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
URL=os.getenv("JS_URL")
CLIENT_SECRET=os.getenv("JS_CLIENT_SECRET")
CLIENT_ID=os.getenv("JS_CLIENT_ID")
SCOPE=os.getenv("JS_SCOPE")
TOKEN_ENDPOINT=os.getenv("JS_TOKEN_ENDPOINT")
AUTHORIZE_ENDPOINT=os.getenv("JS_AUTHORIZE_ENDPOINT")

oauth2client = OAuth2Client(token_endpoint=TOKEN_ENDPOINT, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
token = oauth2client.client_credentials(scope=SCOPE)

from journey_service_client.journey_service_client import AuthenticatedClient
client = AuthenticatedClient(base_url=URL, token=token)


def get_place_by_name(name):
    from journey_service_client.journey_service_client.api.places_v3 import get_stop_places
    from journey_service_client.journey_service_client.models.get_stop_places_sort_order import GetStopPlacesSortOrder
    r = get_stop_places.sync(client=client, name_match=name, sort_order=GetStopPlacesSortOrder("WEIGHT"), limit=1)
    return r.stop_places[0]

def get_trip_between_place_ids(start_id, dest_id, searched_time, time_is_arrival):
    from journey_service_client.journey_service_client.api.trips_v3 import get_trips_by_origin_and_destination
    from journey_service_client.journey_service_client.models.trips_by_origin_and_destination_request_body import TripsByOriginAndDestinationRequestBody

    assert searched_time is None or type(searched_time) is datetime

    r = get_trips_by_origin_and_destination.sync(client=client, 
        json_body=TripsByOriginAndDestinationRequestBody(origin=start_id, 
            destination= dest_id, 
            date=searched_time.date(),
            time=':'.join(str(searched_time.time()).split(":")[:2]),
            for_arrival=time_is_arrival)
        )
    return r.trips

def get_trip_polyline(trip):
    from journey_service_client.journey_service_client.api.trips_v3 import get_trips_by_id

    r = get_trips_by_id.sync(client=client, id=trip.id, include_route_projection=True)
    coordinates = []
    for leg in r.trips[0].legs:
        leg_props = leg.additional_properties
        if "serviceJourney" in leg_props:
            coordinates.extend(leg_props["serviceJourney"]['spatialProjection']['coordinates'])
    return coordinates

def get_map_url_for_trip(trip):
    coordinates = get_trip_polyline(trip)
    return "/static/map/dist/index.html#"+str(coordinates)

def get_trip_departure_time(trip):
    leg_props =trip.legs[0].additional_properties
    if 'start' in leg_props:
        return datetime.fromisoformat(leg_props['start']['timeAimed'])
    return datetime.fromisoformat(leg_props['serviceJourney']['stopPoints'][0]['departure']['timeAimed'])

def get_trip_arrival_time(trip):
    leg_props =trip.legs[-1].additional_properties
    if 'end' in leg_props:
        return datetime.fromisoformat(leg_props['end']['timeAimed'])
    return datetime.fromisoformat(leg_props['serviceJourney']['stopPoints'][-1]['arrival']['timeAimed'])