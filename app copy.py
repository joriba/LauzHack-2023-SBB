from flask import Flask, render_template, request
from markupsafe import Markup
from canton import Canton
from gmaps_helper import geocode, coordinate
from parking_spots_finder import closest_by_car_time, all_trips_for_departure_time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input1 = request.form['user_input1']
        user_input2 = request.form['user_input2']
        user_input3 = request.form['user_input3']
        user_input4 = request.form['user_input4']
        # Process the user input as needed
        origin_lat,  origin_lon = coordinate(user_input1)
        dest_lat, dest_lon = coordinate(user_input2)
        all_trips_for_departure_time(start_time, origin_lat, origin_lon, dest_lat, dest_lon, 5)

        formatted_arr = Markup('<br>'.join(map(str, arr)))

        processed_result = f"Closest train stations to {user_input1} to travel by car: <br> {formatted_arr}"
        return render_template('sbb_result.html', result=processed_result)
    return render_template('sbb_index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


   