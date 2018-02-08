from fhirclient import client
import sqlite3
import datetime
import fhirclient.models.observation as obs
import fhirclient.models.patient as p

class Patient():
    """Patient class is used to house data from fhir and pass it to app.py to be used in the static folders"""
    def __init__(self, *args):
        # YOUR CODE HERE
        self.__name = args[0]
        self.__gender= args[1]
        self.__age = args[2]

    def __str__(self):
        return 'Name: ' + self.__name + '\n' + 'Gender: ' + self.__gender + '\n' + 'Age: ' + self.__age

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

#Define the FHIR Endpoint
settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhirtest.uhn.ca/baseDstu3'
}

#fhirIDs = ['cf-1507072796559','cf-1508283569165', 'cf-1508283628125']

def parse(fhirIDs):
    parsed_patients = []
    #Perform a GET on the fhir patients by id and add them to a patient database
    smart = client.FHIRClient(settings=settings)
    fhirPatients = {}
    for fhirID in fhirIDs:
        fhirPatients[fhirID] = p.Patient.read(fhirID, smart.server)

    for p_id,patient in fhirPatients.items():
        name = patient.name[0].given[0] + " " + patient.name[0].family
        birth = patient.birthDate.isostring.split("-")
        age = str(int(datetime.date.today().year) - int(birth[0]))
        gender = patient.gender
        parsed_patients.append(Patient(name, gender, age))

    return parsed_patients
