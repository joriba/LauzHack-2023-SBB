import gmaps_helper, parkplace_helper
import journey_service_helper
import datetime, time

TRANSFER_TIME = datetime.timedelta(minutes=5)

def car_times_from_parking_spots(origin, parking_spots: list[dict]) -> list[dict]:
    destinations = [[spot.get("lat"), spot.get("lon")] for spot in parking_spots]
    points = gmaps_helper.get_closest_by_car(origin, destinations)
    distances = []
    for i in range(len(destinations)):
        name = points["destination_addresses"][i]
        coords = destinations[i]
        distance = points["rows"][0]["elements"][i]
        distances.append((name, coords, distance))

    return distances

def closest_by_car_time(lat, lon, count):
    result = car_times_from_parking_spots((lat, lon), parkplace_helper.closest_parkings(lat, lon, count))
    result.sort(key=lambda x: x[2]["duration"]["value"])
    return result

def all_trips_for_arrival_time(arrival_time, origin_lat, origin_lon, dest_lat, dest_lon, nb_parkings):
    closest = closest_by_car_time(origin_lat, origin_lon, nb_parkings)
    result = []
    for spot in closest:
        coords = spot[1]
        origin_string = f'{[coords[1], coords[0]]}'.replace(" ", "")
        dest_string = f'{[dest_lon, dest_lat]}'.replace(" ", "")
        trips = journey_service_helper.get_trip_between_place_ids(origin_string, dest_string, arrival_time, True)
        for trip in trips:
            departure_time = journey_service_helper.get_trip_departure_time(trip)
            car_arrival_time = departure_time - TRANSFER_TIME
            car_departure_time = car_arrival_time - datetime.timedelta(seconds=spot[2]["duration"]["value"])
            total_arrival_time = journey_service_helper.get_trip_arrival_time(trip)
            result.append({
                "Departure Time": car_departure_time,
                "Arrival Time": total_arrival_time,
                "Total Duration": total_arrival_time - car_departure_time,
                "Parking Spot": spot[0],
                "Distance by Car": spot[2]
            }) 
        
    return result

def all_trips_for_departure_time(start_time, origin_lat, origin_lon, dest_lat, dest_lon, nb_parkings):
    closest = closest_by_car_time(origin_lat, origin_lon, nb_parkings)
    result = []
    for spot in closest:
        coords = spot[1]
        origin_string = f'{[coords[1], coords[0]]}'.replace(" ", "")
        dest_string = f'{[dest_lon, dest_lat]}'.replace(" ", "")
        train_departure_time = start_time + datetime.timedelta(seconds=spot[2]["duration"]["value"]) + TRANSFER_TIME
        trips = journey_service_helper.get_trip_between_place_ids(origin_string, dest_string, train_departure_time, False)
        for trip in trips:
            arrival_time = journey_service_helper.get_trip_arrival_time(trip)
            train_departure_time = journey_service_helper.get_trip_departure_time(trip)
            car_arrival_time = train_departure_time - TRANSFER_TIME
            car_departure_time = car_arrival_time - datetime.timedelta(seconds=spot[2]["duration"]["value"])
            result.append({
                "Departure Time": car_departure_time,
                "Arrival Time": arrival_time,
                "Total Duration": arrival_time - car_departure_time,
                "Parking Spot": spot[0],
                "Distance by Car": spot[2]
            }) 
        
    return result

# now = datetime.datetime.fromtimestamp(time.time())
# this_afternoon = now - datetime.timedelta(hours=8)
# coords_lausanne = gmaps_helper.coordinate("Arnex")
# coords_bolligen = gmaps_helper.coordinate("St. Gallen")
# # trips = all_trips_for_arrival_time(now, coords_lausanne[0], coords_lausanne[1], coords_bolligen[0], coords_bolligen[1], 2)
# # for trip in trips:
# print("By departure time:")
# trips = all_trips_for_departure_time(now, coords_lausanne[0], coords_lausanne[1], coords_bolligen[0], coords_bolligen[1], 2)
# for trip in trips:
#     print(trip, "\n")
# print("By arrival time:")
# trips = all_trips_for_arrival_time(now, coords_lausanne[0], coords_lausanne[1], coords_bolligen[0], coords_bolligen[1], 2)
# print(trips[0], "\n")
# print(closest_parkings(46.5203, 6.566, 10))
# 46.9467632, 7.4409836
# coords = gmaps_helper.geocode("Chem. des Fleurs de Lys, 1350 Orbe")[0]['geometry']['location']
# print(parkplace_helper.closest_parkings(coords["lat"], coords["lng"], 1000))