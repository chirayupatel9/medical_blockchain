from typing import List, Any

from db_config import block_db, patients, doctor
import re

DOCTOR_USER_SCHEMA = {
    "_id": "5fe6323443a9a0cb53917487",
    "name": "jondoe",
    "type": "Dentist",
    "specialist": "ortho-dentist",
    "location": "valsad",
    "number": "123456",
}

PATIENT_SCHEMA = {
    "patientname": "jondoe",
    "patientnumber": "12345",
    "patientage": "25",
    "diease": "fever",
    "prev_block_hash": ""
}

block_counts = block_db.list_collection_names()
CURRENT_BLOCK = len(block_counts)


# Function to create a doctor
# Parameters : doctor_set dictionary object
def add_doctor(userdoctor):
    query = {"name": userdoctor["name"]}
    if doctor.count_documents(query) == 1:
        return None
    x = doctor.insert_one(userdoctor)
    return x.inserted_id, print('done')


# Function to create a patient
# Parameters : patient_set dictionary object
def add_patient(addpatient):
    query = {"patientname": addpatient["patientname"]}
    if patients.count_documents(query) == 1:
        return None
    x = patients.insert_one(addpatient)
    return x.inserted_id, print('done')


def fetch_prev_block():
    all_pat = patients.find()
    res = []
    for patient in all_pat:
        patient["prev_block_hash"] = str(patient["prev_block_hash"])
        res.append(patient["prev_block_hash"])
    return res[-1]


fetch_prev_block()


# try to fetch cb from database


# ADDING TRANSACTION AND A BLOCK AFTER EVERY 10 TRANSACTIONS.
def add_transaction(inter):
    blocks = block_db.list_collection_names()
    block_count = blocks
    print(blocks)
    block_count = block_count[-1:]
    block_count = str(block_count)
    block_count = block_count.split('transactions')[1].split("'")[0]
    block_count = int(block_count)
    print(block_count)
    current_block = block_count
    print("current block", current_block)
    transactions = block_db[str('transactions' + str(current_block))]
    all_trans = transactions.find()
    total_transactions = []
    query = {"transactions": inter["transactions"]}

    if transactions.count_documents(query) == 1:
        return None

    for transaction in all_trans:
        transaction["transactions"] = str(transaction["transactions"])
        total_transactions.append(transaction["transactions"])
    print('total len and total trans', len(blocks), len(total_transactions))

    if len(total_transactions) < 10:
        x = transactions.insert_one(inter)
        print(total_transactions)
        x.inserted_id, print('inserted done')
    else:
        current_block += 1
        transactions = block_db[str('transactions' + str(current_block))]
        print("current block incremented", current_block)
        x = transactions.insert_one(inter)
        x.inserted_id, print('inserted done to new block')

    return print("done")


tas = {"transactions": 'genesis'}

# add_transaction(tas)
# now adding integrity to blockchain so create a new table with same transaction hash so
# it will be easy for checking its integrity
