# Adds Doctors
import dbconnect
import hashlib
import json
from transactions import add_transaction


def add_doctor(doctorname, doc_type, specialist, location, number):
    prev_block_hash = str(hashlib.md5(dbconnect.fetch_prev_doctor_block().encode()).hexdigest())
    data = {
        "name": doctorname,
        "type": doc_type,
        "specialist": specialist,
        "location": location,
        "number": number,
        "prev_block_hash": prev_block_hash,
    }

    # print(data)
    current_block_hash = str(hashlib.md5(str(data).encode()).hexdigest())
    transactions = {
        "prev_block_hash": prev_block_hash,
        'current_block_hash': current_block_hash,
    }
    print(transactions, '::', prev_block_hash)
    # dbconnect.add_doctor(data)
    # add_transaction(transactions)
    return json.dumps(data)

add_doctor('chirayu','computer','dontknow','valsad',123)
