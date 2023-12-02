import gmaps_helper, parkplace_helper

def car_times_from_parking_spots(origin, parking_spots: list[dict]) -> list[dict]:
    destinations = [[spot.get("lat"), spot.get("lon")] for spot in parking_spots]
    points = gmaps_helper.get_closest_by_car(origin, destinations)
    distances = []
    for i in range(len(destinations)):
        name = points["destination_addresses"][i]
        coords = destinations[i]
        distance = points["rows"][0]["elements"][i]["duration"]
        distances.append((name, coords, distance))

    return distances

def closest_by_car_time(lat, lon, count):
    result = car_times_from_parking_spots((lat, lon), parkplace_helper.closest_parkings(lat, lon, count))
    result.sort(key=lambda x: x[2]["value"])
    return result