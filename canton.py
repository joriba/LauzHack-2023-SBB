import journey_service_helper

def Canton(city):
    canton = journey_service_helper.get_place_by_name(city).canton
    b = journey_service_helper.get_place_by_name(city).centroid
    return canton, b

