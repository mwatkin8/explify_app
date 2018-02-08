"""app.py initiates the flask webapp and renders the html contained in the templates folder."""
from flask import Flask, render_template
import os
import fhirParser

# create the application object
APP = Flask(__name__, static_folder='static')

@APP.route('/', methods=['GET'])
def home():
    """
    Renders index.html
    """
    pp = fhirParser.parse(['cf-1507072796559','cf-1508283569165', 'cf-1508283628125'])
    out = ""
    for patient in pp:
        out = out + patient.__str__() + '\n'

    return render_template('index.html',object=out)

# start the server with the 'run()' method
if __name__ == '__main__':
    APP.run(debug=True, host="0.0.0.0")
