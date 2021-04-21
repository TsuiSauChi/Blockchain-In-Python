import hashlib

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None 
        self.prev = None

    def setKey(self, key):
        self.key = key

# Store Each MerkelTree Value in a Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert Node at the end of list
    def insert(self, key):
        node = Node(key)
        if self.head == None:
            self.head = self.tail = node
        else:
            temp = self.head
            while temp is not None:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = node
            node.prev = temp
            # Node is dependent on previous node
            node.setKey(self.hash(node))
        return self

    # Create Key based on prev Node key
    def hash(self, node):
        hasher = hashlib.sha256()
        hasher.update(str.encode(node.key + node.prev.key))
        return hasher.hexdigest()

    # Return the entire Linked List
    def getList(self):
        temp = self.head 
        blockchain = list()
        while temp is not None:
            blockchain.append(temp.key)
            temp = temp.next
        return blockchain

class MerkelTree:
    def __init__(self):
        self.root = None

    def createMerkelHash(self, blocks):
        list_len = len(blocks)
        while len(blocks) != 1:
            # Ensure that the list is of even number
            while (list_len % 2) != 0:
                blocks.extend(blocks[-1:])
                list_len = len(blocks)

            # Iteratively hash a pair of value untils a single hash value
            secondary = list()
            for k in [blocks[x:x+2] for x in range(0, len(blocks), 2)]:
                hasher = hashlib.sha256()
                hasher.update(str.encode(k[0]+k[1]))
                secondary.append(hasher.hexdigest())       
            blocks = secondary   

        return blocks[0]

# Modifiction of Stack to store data
class DataList:
    def __init__(self):
        self.index = -1
        self.data = list()

    def add(self, value):
        self.index += 1
        self.data.append(value)

    def delete(self, value):
        if self.isEmpty():
            print("Data Block is Empty")
        else:
            self.data.remove(value)

    def isEmpty(self):
        if self.index == -1:
            return True
        else:
            return False

    def sort(self):
        self.data = sorted(self.data)
        return self.data

    def getList(self):
        return self.data

newMerkel = MerkelTree()

# First Block
newList1 = DataList()
newList1.add('C')
newList1.add('B')
newList1.add('A')
newList1.delete('C')
newList1.sort()
print(newList1.getList())
hash_value1 = newMerkel.createMerkelHash(newList1.getList())
print(hash_value1)

# Second Block
newList2 = DataList()
newList2.add('1')
newList2.add('2')
print(newList2.getList())
hash_value2 = newMerkel.createMerkelHash(newList2.getList())
print(hash_value2)

# Third Block
newList3 = DataList()
newList3.add('This is a Test')
newList3.add('Hello World')
print(newList3.getList())
hash_value3 = newMerkel.createMerkelHash(newList2.getList())
print(hash_value3)

print()

# Create Sample Blockchain
ll = DoublyLinkedList()
print("Blockchain Created")
ll.insert(hash_value1)
ll.insert(hash_value2)
ll.insert(hash_value3)
print(ll.getList())


