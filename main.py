from Block import Block

blockchain = []
patient_name = input("Pname")
pat_number = input("pnum")
genesis_block = Block(patient_name, pat_number)

second_block = Block(genesis_block.block_hash, [input("pname1"), input("pnum1")])

third_block = Block(second_block.block_hash, ["adfsfas", "sdfasf"])
print(genesis_block.block_hash)
print(genesis_block)

print(second_block.transactions)
print(third_block.transactions)
