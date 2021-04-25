# Modifiction of Queue to store data

import sys

class Mempool:
    def __init__(self):
        self.index = -1
        self.pool = list()

    def add(self, value):
        self.index += 1
        self.pool.append(value)
        return self

    def deleteblock(self, block):
        try:
            for i in block:
                self.pool.remove(i)
            self.index -= len(block)
        except:
            print("Pool does not contain data")

    def delete(self, value):
        if self.isEmpty():
            print("Pool is Empty")
        else:
            self.index -= 1
            self.pool.remove(value)

    def isEmpty(self):
        if self.index == -1:
            return True
        else:
            return False

    def sort(self):
        self.pool = sorted(self.pool)
        return self.pool

    def get(self, index):
        return self.pool[index]

    def getIndex(self):
        return self.index

    def getPool(self):
        return self.pool

# Class to validate data in memory pool
# Based on FIFO
class ValidateBlock:
    def __init__(self):
        self.block = list()

    def curate(self, pool, size):
        index = 0
        while (int(pool.getIndex() - index) != -1) and (sys.getsizeof(self.block) != size):
            self.block.append(pool.get(index))
            index += 1
        return self.block
    
    def updatepool(self, pool, block):
        pool.deleteblock(block)


