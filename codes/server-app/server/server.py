from flask import Flask, request, jsonify
import util

"""from util import get_location_names
from util import get_estimated_price"""

app = Flask(__name__)

#__loc = None
#return available locacions
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    ### get inputs from form
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask server for home price prediction ")
    util.load_save_artifacts()
    #__loc = util.get_location_names()

    #util.get_location_names()
    #print(__loc)
    app.run()