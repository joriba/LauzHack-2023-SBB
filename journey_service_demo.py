from journey_service_helper import get_place_by_name, get_trip_between_place_ids

geneva_id = get_place_by_name("Genève").id
zurich_id = get_place_by_name("Zürich").id

print(geneva_id, zurich_id)

trip = get_trip_between_place_ids(geneva_id, zurich_id)
print([x.duration for x in trip.legs])