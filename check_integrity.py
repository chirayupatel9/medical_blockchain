import re
import hashlib
from db_config import block_db, patients
import dbconnect


def check_integrity():
    results = []
    blocks = block_db.list_collection_names()
    current_block = int(re.findall(r"\d+", block_db.list_collection_names()[-1])[0])
    print("current block = ", current_block)
    transactions = block_db[str('transactions' + str(current_block))]
    all_trans = transactions.find()
    all_patients = patients.find()
    prev_block_hash = []
    total_transactions = []
    for transaction in all_trans:
        for patient in all_patients:
            transaction["transactions"] = str(transaction["transactions"])
            patient["prev_block_hash"] = str(patient["prev_block_hash"])
            prev_hash = patient
            actual_hash = transaction['transactions']
            print("pre and ac", prev_hash, ':;:', actual_hash)
        # print(transaction['transactions'])
        total_transactions.append(transaction["transactions"])
    print('total len and total trans', len(blocks), len(total_transactions))
    # delete these lines afterwords
    print("total transactions are", total_transactions)

    return results


check_integrity()
