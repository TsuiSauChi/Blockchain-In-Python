import hashlib
from block import Block
import consensus.pow as consensus

# Store Each MerkelTree Value in a Linked List
class Blockchain:
    def __init__(self):
        self.difficulty = 5
        self.head = None
        self.tail = None

    # Insert block at the end of list
    def insert(self, key, nonceValue):
        block = Block(key)
        if self.head == None:
            self.head = self.tail = block
        else:
            # Check if the nonceValue is accurate; if yes, append a new 
            # block at the end of the list 
            # Note: The pow check and the block key does not match, hence 
            # the blockchain key takes the previous block's key into account 
            if consensus.check(self.hash(block, nonceValue, True), self.difficulty):
                temp = self.head
                while temp is not None:
                    if temp.next is None:
                        break
                    temp = temp.next
                temp.next = block
                block.prev = temp
                block.setKey(self.hash(block, nonceValue, False))
            else:
                print("Nonce value is incorrect")
        return self
    
    # Mining for nonceVlaue using POW consensus
    def mine(self, key):
        nonceValue = consensus.pow(key, self.difficulty)
        return nonceValue

    # Function to check & create hash key
    def hash(self, block, nonceValue, checkFlag):
        hasher = hashlib.sha256()
        if checkFlag is True:
            hasher.update(str.encode(block.key + str(nonceValue)))
        else:  
            hasher.update(str.encode(block.key + block.prev.key + str(nonceValue)))
        return hasher.hexdigest()

    # Return the entire Linked List
    def getList(self):
        temp = self.head 
        blockchain = list()
        while temp is not None:
            blockchain.append(temp.key)
            temp = temp.next
        return blockchain