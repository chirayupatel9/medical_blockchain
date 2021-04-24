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
        transaction["prev_block_hash"] = str(transaction["prev_block_hash"])
        actual_hash = transaction['prev_block_hash']
        print(':;:', actual_hash)
        total_transactions.append(transaction["prev_block_hash"])
    for patient in all_patients:
        patient["prev_block_hash"] = str(patient["prev_block_hash"])
        prev_block_hash = patient['prev_block_hash']
        print(prev_block_hash)



    print('total len and total trans', len(blocks), len(total_transactions))
    # delete these lines afterwords
    # print("total transactions are", total_transactions)

    return results


check_integrity()
