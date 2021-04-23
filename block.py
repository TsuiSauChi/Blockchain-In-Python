class Block:
    height = 0

    def __init__(self, key):
        self.key = key
        self.next = None 
        self.prev = None
        self.nonce = 0
        self.height = Block.height
        Block.height += 1

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getNonce(self):
        return self.nonce

    def setNonce(self, nonce):
        self.nonce = nonce

    def getPrevBlock(self):
        return self.prev