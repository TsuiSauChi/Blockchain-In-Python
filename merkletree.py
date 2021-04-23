import hashlib

class MerkelTree:
    def __init__(self):
        self.root = None

    def createMerkelHash(self, blocks):
        list_len = len(blocks)
        # Counter to ensure hashing if the block list is 1
        counter = 0
        while len(blocks) != 1 or counter is 0:
            counter += 1
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