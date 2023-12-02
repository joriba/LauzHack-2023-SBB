from flask import Flask, render_template, request
from markupsafe import Markup
from canton import Canton
from gmaps_helper import geocode
from parking_spots_finder import closest_by_car_time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input1 = request.form['user_input1']
        user_input2 = request.form['user_input2']
        user_input3 = request.form['user_input3']
        # Process the user input as needed
        coords = geocode(user_input1)[0]['geometry']['location']
        arr = [(sub_array[0] + ' ' + sub_array[2]['text']) for sub_array in closest_by_car_time(coords['lat'], coords['lng'], 7)]

        formatted_arr = Markup('<br>'.join(map(str, arr)))

        processed_result = f"Closest train stations to {user_input1} to travel by car: <br> {formatted_arr}"
        return render_template('sbb_result.html', result=processed_result)
    return render_template('sbb_index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


   