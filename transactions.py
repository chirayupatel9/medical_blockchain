from db_config import block_db

genesis_transaction = {"prev_block_hash": 'genesis1',
                       'current_block_hash': 'genesis1', }


# ADDING TRANSACTION AND A BLOCK AFTER EVERY 10 TRANSACTIONS. Delete all print statement
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
    for transaction in all_trans:
        transaction["prev_block_hash"] = str(transaction["prev_block_hash"])
        total_transactions.append(transaction["prev_block_hash"])
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

# add_transaction(genesis_transaction)
