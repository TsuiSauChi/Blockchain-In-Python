from blockchain import Blockchain
from block import Block
from mempool import Mempool
from merkletree import MerkelTree

import hashlib

newMerkel = MerkelTree()
ll = Blockchain()

# First Block: is genesis block
newList1 = Mempool()
newList1.add('Genesis Block')
newList1.sort()
hash_value1 = newMerkel.createMerkelHash(newList1.getList())

# Add genesis block into the blockchain
ll.insert(hash_value1, 0)

# Second Block
newList2 = Mempool()
newList2.add('1')
newList2.add('2')
hash_value2 = newMerkel.createMerkelHash(newList2.getList())

nonceValue = ll.mine(hash_value2)
ll.insert(hash_value2, nonceValue)

# Third Block
newList3 = Mempool()
newList3.add('This is a Test')
newList3.add('Hello World')
hash_value3 = newMerkel.createMerkelHash(newList3.getList())

nonceValue = ll.mine(hash_value3)
ll.insert(hash_value3, nonceValue)

print()


blockchain = ll.getList()
print(blockchain)
