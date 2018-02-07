"""app.py initiates the flask webapp and renders the html contained in the
templates folder.
"""
from flask import Flask, render_template
import os
import fhirParser


# create the application object
APP = Flask(__name__, static_folder='static')

#Define the FHIR Endpoint
settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhirtest.uhn.ca/baseDstu3'
}
smart = client.FHIRClient(settings=settings)

@APP.route('/', methods=['GET'])
def home():
    """
    Renders index.html
    """
    return render_template('index.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    APP.run(debug=True, host="0.0.0.0")
