from dotenv import load_dotenv
import os

load_dotenv()
JM_URL=os.getenv("JM_URL")
JM_API_KEY=os.getenv("JM_API_KEY")
LANG=os.getenv("GLOABL_LANG","en")

from journey_maps_client.journey_maps_client import Client
client = Client(base_url=JM_URL, httpx_args={"params":{"api_key":JM_API_KEY}})

def get_journey_for_trip_id(trip_id):
    from journey_maps_client.journey_maps_client.api.journey_api import journey_get 
    from journey_maps_client.journey_maps_client.models.journey_get_lang import JourneyGetLang

    r = journey_get.sync_detailed(client=client, ctx=trip_id, lang=JourneyGetLang(LANG))
    return r.parsed