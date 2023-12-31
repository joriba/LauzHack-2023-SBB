from flask import Flask, render_template, request
from markupsafe import Markup
from canton import Canton
from gmaps_helper import geocode, coordinate
from parking_spots_finder import closest_by_car_time, all_trips_for_departure_time, all_trips_for_arrival_time
from gmaps_helper import get_travel_time_by_car
from journey_service_helper import get_map_url_for_trip
import datetime
import time
from datetime import datetime
from hashlib import sha256

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input1 = request.form['user_input1']
        user_input2 = request.form['user_input2']
        user_input3 = request.form['user_input3']
        user_input4 = request.form['user_input4']
        criterium = request.form['sorting_criterion']

        print(criterium)

        arrival_time = None
        current = False
        
        date_format = "%Y-%m-%dT%H:%M"

        if user_input3 != "":
            start_time = datetime.strptime(user_input3, date_format)
        else:
            start_time = datetime.now()
            current = True

        if user_input4 != "":
            user_input4 = datetime.strptime(user_input4, date_format)
            arrival_time = user_input4

        origin_lat,  origin_lon = coordinate(user_input1)
        dest_lat, dest_lon = coordinate(user_input2)

        if current:
            if arrival_time is not None:
                arr = all_trips_for_arrival_time(arrival_time, origin_lat, origin_lon, dest_lat, dest_lon, 5)
            else:
                arr = all_trips_for_departure_time(start_time, origin_lat, origin_lon, dest_lat, dest_lon, 5)
        if not current:
            arr = all_trips_for_departure_time(start_time, origin_lat, origin_lon, dest_lat, dest_lon, 5)
        
        car_info = get_travel_time_by_car((origin_lat, origin_lon), (dest_lat, dest_lon))
        print(car_info)
        non_eco = car_info['distance']['value']
        
        if not arr:
            return render_template('sbb_result.html', result="Could not find any journeys.")
            # does not work - problem: 
            # File "/home/natali/Desktop/hackathon/LauzHack-2023-SBB/journey_service_helper.py", line 41, in get_trip_between_place_ids return r.trips

        # formatted_arr = Markup('<br>'.join(map(str, arr)))
        arr = choose(arr, criterium=criterium)[:3]


        # formatting:

        formatted_arr = [
            f'<details{" open" if i == 0 else ""}>'
                '<summary>'
                f'<div style="border: 1px solid lightgray; padding: 10px;">'
                f'Departure time: {el["Departure Time"].strftime("%Y-%m-%d %H:%M:%S %z")[:-6]}'
                f'<br> Arrival time: {el["Arrival Time"].strftime("%Y-%m-%d %H:%M:%S %z")[:-6]}'
                f'<br> Parking spot: {el["Parking Spot"]}'
                f'<br> Distance to be traveled by car: {el["Distance by Car"]["distance"]["text"]}'
                f"<br> Duration of the trip: {el['Total Duration']}"
                f'<span style="color: red;"> <br> Duration by car instead for the whole journey: {car_info["duration"]["text"]} </span>'
                f'<span style="color: green;"> <br> This trip is: {round((car_info["distance"]["value"] - el["Distance by Car"]["distance"]["value"])/(car_info["distance"]["value"] + 1) * 100, 2)}% more energy efficient</span>'
                f'</div>'
                '</summary>'
                f'<br> <iframe width="800px" height="600px" src="{get_map_url_for_trip(el["TripData"], el["Car Polyline"])}"></iframe>' 
            '</details>'
            for i,el in enumerate(arr)
            ]

        f_arr = Markup('<br> <br> <br>'.join(map(str, formatted_arr)))

        # processed_result = f"Closest train stations to {user_input1} to travel by car: <br> {f_arr}"
        return render_template('sbb_result.html', result=f_arr)

    return render_template('sbb_index.html')


def choose(arr, criterium=''):
    #duration, distance by car
    if criterium == 'total_duration':
        return sorted(arr, key=lambda x: x['Total Duration'])
    if criterium == "duration_by_car":
        return sorted(arr, key=lambda x: (x['Distance by Car']['distance']['value'], x['Total Duration']))
    if criterium == "arrival_time":
        return sorted(arr, key=lambda x: (x['Arrival Time']))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")