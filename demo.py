from journey_service_helper import get_place_by_name, get_trip_between_place_ids
from journey_maps_helper import get_journey_for_trip_id
from gmaps_helper import get_closest_by_car
from gmaps_helper import geocode

geneva_id = get_place_by_name("Genève").id
zurich_id = get_place_by_name("Zürich").id

print(geneva_id, zurich_id)

trip = get_trip_between_place_ids(geneva_id, zurich_id)
print([x.duration for x in trip.legs])

r = get_journey_for_trip_id(trip.id)
print(len(r.features))

distances = get_closest_by_car("1020 Renens", ["Lausanne"])
print(distances)

location = geocode("Lausanne")
print(location)
