import json

from flask import jsonify
from bson.json_util import dumps, loads
from db_config import patients, doctors, admin

DOCTOR_USER_SCHEMA = {
    "_id": "60756d56c44fb6fd55337f82",
    "name": "jondoe",
    "type": "Dentist",
    "specialist": "ortho-dentist",
    "location": "valsad",
    "number": "123456",
}

PATIENT_SCHEMA = {
    "_id": "60756d56c44fb6fd55337f82",
    "patientname": "jondoe2",
    "patientnumber": "12345",
    "patientage": "25",
    "diease": "fever",
    "doctor_assigned": {
        "doctorname": "whatever",
        "doctor_notes": "whatever",
    }
}
ADMIN_SCHEMA = {
    "name": "jondoe1",
    'email': 'abc@abc.com',
    "password": "123451",
    "confirm_password": "123451"
}


# Function to create a doctor
# Parameters : doctor_set dictionary object
def add_doctor_to_db(userdoctor):
    query = {"doctorname": userdoctor["doctorname"]}
    if doctors.count_documents(query) == 1:
        return None
    x = doctors.insert_one(userdoctor)
    return print('done')


# add_doctor_to_db(DOCTOR_USER_SCHEMA)

# Function to create a patient
# Parameters : patient_set dictionary object
def add_patient_to_db(addpatient):
    query = {"patientname": addpatient["patientname"]}
    if patients.count_documents(query) == 1:
        return None
    x = patients.insert_one(addpatient)
    return x


# add_patient_to_db(PATIENT_SCHEMA)


# Function for Updating the patient
# Parameters : patient_set dictionary object
def updating_patient(updatepat):
    query = {"patientname": updatepat["patientname"]}
    if patients.count_documents(query) == 1:
        x = patients.replace_one(query, updatepat)
    return 'done'


def assigned_doc_to_pat(pat):
    query = {'patientname': pat['patientname']}
    if patients.count_documents(query) == 1:
        x = patients.update_one(query, {"$set": {"doctor_assigned": {"doctorname": pat['doctorname'],
                                                                     "doctor_notes": pat['doctor_notes'], }}})
    return 'done'


patna = {
    'patientname': 'jondoe1', 'doctorname': 'doctor 2', "doctor_notes": 'corona'
}
# assigned_doc_to_pat(patna)


# updating_patient(PATIENT_SCHEMA)

# Function for Updating the patient
# Parameters : patient_set dictionary object
def fetch_all_patient():
    fap = patients.find({})
    list_cur = list(fap)
    json_data = dumps(list_cur)
    return json_data


# print(fetch_all_patient())
def fetch_patient(pname):
    fap = patients.find_one({'patientname': pname})
    json_data = dumps(fap)
    return json_data


# print(fetch_all_patient())


# now adding integrity to blockchain so create a new table with same transaction hash so
# it will be easy for checking its integrity
def adding_admin(adm):
    query = {"name": adm["name"]}
    if admin.count_documents(query) == 1:
        return print("already there")
    if [{"password": adm["password"]} == {"confirm_password": adm["confirm_password"]}]:
        x = admin.insert_one(adm)
    return print('done')


# adding_admin(ADMIN_SCHEMA)
def fetch_admin(adm):
    query = {"name": adm["name"]}
    cred = {'name': adm["name"],
            'password': adm['password']}
    done = 1
    if admin.count_documents(query) == 0:
        response = {'message': "Account doesn't exists and Create a new Account"}
        return False
    return True

# fetch_admin(ADMIN)
