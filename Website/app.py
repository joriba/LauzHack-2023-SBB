from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Process the user input as needed
        processed_result = f'You entered: {user_input}'
        return render_template('result.html', result=processed_result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")