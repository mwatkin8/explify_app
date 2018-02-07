from fhirclient import client
import datetime
import fhirclient.models.observation as obs
import fhirclient.models.patient as p

#Define the FHIR Endpoint
settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhirtest.uhn.ca/baseDstu3'
}
smart = client.FHIRClient(settings=settings)

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

#Perform a GET on the Test siblings by id and add them to a patient dictionary
fhirPatients = {}
fhirPatients['cf-1507072796559'] = p.Patient.read('cf-1507072796559', smart.server)
fhirPatients['cf-1508283569165'] = p.Patient.read('cf-1508283569165', smart.server)
fhirPatients['cf-1508283628125'] = p.Patient.read('cf-1508283628125', smart.server)

patients = []
for p_id,p in fhirPatients.items():
    name = p.name[0].given[0] + p.name[0].family
    birth = p.birthDate.isostring.split("-")
    age = str(int(datetime.date.today().year) - int(birth[0]))
    patients[p_id] = Patient(name, gender, age)

for patient in patients:
    print(patient.__str__())
