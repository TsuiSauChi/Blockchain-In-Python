from blockchain import Blockchain
from block import Block
from mempool import Mempool
from mempool import ValidateBlock
from merkletree import MerkelTree
from application.identity import Identity
from application.transaction import Transaction

import hashlib, random

# Set Initialization Variables 
block_size = 120 
difficulty = 4

def main():
    newMerkel = MerkelTree()
    ll = Blockchain(difficulty)

    # First Block: is genesis block
    hash_value1 = newMerkel.createMerkelHash(['Genesis Block'])
    # Add genesis block into the blockchain
    ll.insert(hash_value1, 0)

    # Create new identity
    James = Identity()

    # Create Memory Pool with random values
    pool = Mempool()
    for i in range(100):
        new_transaction = Transaction(James, random.randrange(1,100))
        new_transaction.sign(James.getPrivateKey())
        pool.add(new_transaction)


    # Loop until memory pool is empty
    while pool.isEmpty() is False:
        # 1. Create an instance to validate block
        validate_block = ValidateBlock()
        # 2. Get a subset of memory block to validate
        block = validate_block.curate(pool, block_size)
        # 3. Run Markle tree on block to be validated
        hash_value2 = newMerkel.createMerkelHash(block)
        # 4. Mine Block using POS consensus
        nonceValue = ll.mine(hash_value2)
        # 5. Insert new block into the blockchain
        ll.insert(hash_value2, nonceValue)
        # 6. Update the memory pool
        validate_block.updatepool(pool, block)
        print("Pool:", pool.getPool())
        print()

    print()

    print("Blockchain:")
    ll.getList()

if __name__ == "__main__":
    main()