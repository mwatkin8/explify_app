"""app.py initiates the flask webapp and renders the html contained in the
templates folder.
"""
from flask import Flask, render_template
from fhirclient import client
import os
import datetime
import fhirclient.models.observation as obs
import fhirclient.models.patient as p
#import fhirParser


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
    #Perform a GET on the Test siblings by id and add them to a patient dictionary
    fhirPatients = {}
    #fhirPatients['cf-1507072796559'] = p.Patient.read('cf-1507072796559', smart.server)
    #fhirPatients['cf-1508283569165'] = p.Patient.read('cf-1508283569165', smart.server)
    #fhirPatients['cf-1508283628125'] = p.Patient.read('cf-1508283628125', smart.server)

    patients = []
    for p_id,p in fhirPatients.items():
        name = p.name[0].given[0] + p.name[0].family
        birth = p.birthDate.isostring.split("-")
        age = str(int(datetime.date.today().year) - int(birth[0]))
        patients[p_id] = Patient(name, gender, age)

    for patient in patients:
        print(patient.__str__())

    return render_template('index.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    APP.run(debug=True, host="0.0.0.0")
