import socket, os

# Simulate new Block
class Block:
    height = 0

    def __init__(self):
        self.key = "p422955edcc1ccfc017761404fa54e784c225c56e2db7426fdc02a4df2994ed1"
        self.next = None 
        self.prev = "422955edcc1ccfc017761404fa54e784c225c56e2db7426fdc02a4df2994ed12"
        self.nonce = 0

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

newBlock = Block()

class Client:

    def __init__(self):
        serverName = ""
        serverPort = 10000
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((serverName, serverPort))

    def initalization(self):
        self.clientSocket.send(str.encode("INIT"))
        height = self.clientSocket.recv(1).decode()
        
        filename = os.getcwd() + "/blockchain.txt"
        with open(filename,'a') as file_append:
            for _ in range(int(height)):
                block = self.clientSocket.recv(64).decode()
                file_append.write(block + "\n")
            file_append.close()
        print("BlockChain Initialized")
        return


    def broadcast_block(self, block):
        self.clientSocket.send(str.encode("CAST"))
        # Need to change to block.prev.key 
        self.clientSocket.send(str.encode(block.prev))
        # Receive status code - whether new block is valid
        status = self.clientSocket.recv(3).decode()
        print("Testing")
        if status == "200":
            print("Block is Valid")
            self.clientSocket.send(str.encode(block.key))
        else:
            print("Block is not Valid")

    # Reset Blockchain
    def reset(self):
        filename = os.getcwd() + "/blockchain.txt"
        file = open(filename, "r+")
        file.truncate(0)
        file.close()
    
    def close(self):
        self.clientSocket.close()


newClient = Client()
newClient.reset()
newClient.initalization()
newClient.close()

newClient = Client()
newClient.broadcast_block(newBlock)
newClient.close()