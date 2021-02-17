# Adds Patients
import dbconnect
import hashlib
import json


def write_patient_transaction(patientname, patientnumber, patientage, diease):
    prev_block_hash = str(hashlib.md5(dbconnect.fetch_prev_block().encode()).hexdigest())
    data = {
        "patientname": patientname,
        "patientnumber": patientnumber,
        "patientage": patientage,
        "diease": diease,
        "prev_block_hash": prev_block_hash,
    }
    # print(data)
    transactions = {
        "transactions": prev_block_hash,
    }
    dbconnect.add_patient(data)
    dbconnect.add_transaction(transactions)
    return json.dumps(data)


write_patient_transaction('chirayhjunpvhatel', 3234, 3, 'co')
