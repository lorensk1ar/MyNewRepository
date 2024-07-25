## MODULES
from flask import Flask, render_template, request, jsonify

# create a flask object
app = Flask(__name__)

# initialize a variable for count
counter = 0

# route for index
@app.route('/')
def index():
    return render_template('index.html', counter=counter)

# route to update counter
@app.route('/update', methods=['POST'])
def update_counter():
    global counter
    data = request.get_json()
    if data['action'] == 'increment':
        counter += 1
    elif data['action'] == 'decrement':
        counter -= 1
    return jsonify(counter=counter)

## MAIN
if __name__ == '__main__':
    app.run(debug=True)


