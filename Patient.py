# Adds Patients
import dbconnect
import hashlib
import json
from transactions import add_transaction


def write_patient_transaction(patientname, patientnumber, patientage, diease):
    # prev_block_hash = str(hashlib.md5(dbconnect.fetch_prev_patient_block().encode()).hexdigest())
    prev_block_hash = str(dbconnect.fetch_prev_patient_block())
    data = {
        "patientname": patientname,
        "patientnumber": patientnumber,
        "patientage": patientage,
        "diease": diease,
        "prev_block_hash": prev_block_hash,
    }
    # print(data)
    current_block_hash = str(hashlib.md5(json.dumps(data).encode()).hexdigest())
    transactions = {
        "prev_block_hash": prev_block_hash,
        'current_block_hash': current_block_hash, # think about this
    }
    print(transactions)
    # dbconnect.add_patient(data)
    # add_transaction(transactions)
    return json.dumps(data)


write_patient_transaction('pafsdvrth', 32546434, 3, 'co')
