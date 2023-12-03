from flask import Flask, render_template, request
from canton import Canton
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input1 = request.form['user_input1']
        user_input2 = request.form['user_input2']
        user_input3 = request.form['user_input3']
        # Process the user input as needed
        processed_result = f'Canton of {user_input1} and {user_input2}: {Canton(user_input1), Canton(user_input2),}'
        return render_template('sbb_result.html', result=processed_result)
    return render_template('sbb_index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")