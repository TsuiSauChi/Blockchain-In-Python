import hashlib

class MerkelTree:
    def __init__(self):
        self.root = None

    def createMerkelHash(self, blocks):
        # Copy block to ensure the orginial block is not changed 
        # for future referencing at main.py line 40
        copy_block = blocks.copy()
        list_len = len(copy_block)
        # Counter to ensure hashing if the block list is 1
        counter = 0
        # Ensure that the list is of even number
        while (list_len % 2) != 0:
            copy_block.extend(copy_block[-1:])
            list_len = len(copy_block)

        # Iteratively hash a pair of value untils a single hash value
        secondary = list()
        # error here
        for k in [copy_block[x:x+2] for x in range(0, len(copy_block), 2)]:
            hasher = hashlib.sha256()
            hasher.update(str.encode(str(k[0])+str(k[1])))
            secondary.append(hasher.hexdigest())       
        copy_block = secondary   

        if len(secondary) == 1:
            return secondary[0]
        else:
            return self.createMerkelHash(secondary)

        return copy_block[0]