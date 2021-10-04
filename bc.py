import hashlib

class PyCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

#TRANSACTIONS
t1 = 'A sends 2 PC to B'
t2 = 'B sends 32 PC to M'
t3 = 'D sends 21 PC to K'
t4 = 'A sends 0.2 PC to E'
t5 = 'C sends 2.1 PC to A'
t6 = 'A sends 2.3 PC to B'

#first block
first_block = PyCoinBlock('First', [t1, t2])

print(first_block.block_data)
print(first_block.block_hash)

#second block
second_block = PyCoinBlock(first_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

#third block
third_block = PyCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)