from journey_service_helper import get_place_by_name, get_trip_between_place_ids, get_trip_departure_time, get_trip_arrival_time, get_trip_polyline
from journey_maps_helper import get_journey_for_trip_id
from gmaps_helper import get_closest_by_car, get_travel_time_by_car
from gmaps_helper import geocode
from datetime import datetime, timedelta
import time

geneva_id = get_place_by_name("Genève").id
zurich_id = get_place_by_name("Zürich").id

print(geneva_id, zurich_id)

now = datetime.fromtimestamp(time.time())

trips = get_trip_between_place_ids(geneva_id, zurich_id, now, False)
print(len(trips))
for i, trip in enumerate(trips):
    start_time = get_trip_departure_time(trip)
    end_time = get_trip_arrival_time(trip)
    print("start:",start_time,"end:",end_time)

polyline = get_trip_polyline(trips[-1])
print("Line:",len(polyline))
print(polyline)

r = get_journey_for_trip_id(trip.id)
print(len(r.features))

distances = get_closest_by_car("1020 Renens", ["Lausanne"])
print(distances)

location = geocode("Lausann")
print(location)

car_time = get_travel_time_by_car("Bern", "Lausanne")
print(car_time)
