from flask import Flask, render_template, request
from markupsafe import Markup
from canton import Canton
from gmaps_helper import geocode, coordinate
from parking_spots_finder import closest_by_car_time, all_trips_for_departure_time, all_trips_for_arrival_time
import datetime
import time
from datetime import datetime

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
        
        
        if not arr:
            return render_template('sbb_result.html', result="Could not find any journeys.")
            # does not work - problem: 
            # File "/home/natali/Desktop/hackathon/LauzHack-2023-SBB/journey_service_helper.py", line 41, in get_trip_between_place_ids return r.trips


        print(arr)

        # formatted_arr = Markup('<br>'.join(map(str, arr)))
        arr = choose(arr, criterium=criterium)

        processed_result = f"Closest train stations to {user_input1} to travel by car: <br> {arr}"
        return render_template('sbb_result.html', result=processed_result)
    return render_template('sbb_index.html')


def choose(arr, criterium=''):
    #duration, distance by car, price
    if criterium == 'total_duration':
        return sorted(arr, key=lambda x: x['Total Duration'])
    if criterium == "duration_by_car":
        return sorted(arr, key=lambda x: x['Distance by Car']['duration']['value'])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")