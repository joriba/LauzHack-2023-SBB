import requests
from requests_oauth2client import OAuth2Client, OAuth2ClientCredentialsAuth
from dotenv import load_dotenv
import os

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

def get_trip_between_place_ids(start_id, dest_id):
    from journey_service_client.journey_service_client.api.trips_v3 import get_trips_by_origin_and_destination
    from journey_service_client.journey_service_client.models.trips_by_origin_and_destination_request_body import TripsByOriginAndDestinationRequestBody

    r = get_trips_by_origin_and_destination.sync(client=client, json_body=TripsByOriginAndDestinationRequestBody(origin= start_id, destination= dest_id))
    return r.trips[0]
