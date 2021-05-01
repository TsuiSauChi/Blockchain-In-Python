import socket, csv, os
from threading import Thread

class TCPConnection:
    def __init__(self, host='', port=10001):
        self.host = host
        self.port = port
        self.blockchianFile = os.getcwd() + "/file/blockchain.txt"

    def start(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serverSocket.bind((self.host, self.port))
        serverSocket.listen(5)
        print("Server is listening")

        while True:
            connectionSocket, adr = serverSocket.accept()
            t = Thread(target=self.child, args=(connectionSocket,))
            t.start()

    def child(self, connectionSocket):
        # Check for specific action
        cmd = connectionSocket.recv(4).decode()
        print("Command:", cmd)
        
        if "INIT" in str(cmd):
            print("INIT Peers")
            # Send height metadata to client
            height, blocks = self.initalization()
            connectionSocket.send(str(height).encode())
            print("Sending Blocks")
            for block in blocks:
                # Remove new Line \n
                block = block.strip('\n')
                connectionSocket.send(str(block).encode())

        if "CAST" in str(cmd):
            print("Listening for new Block")
            prev_block = connectionSocket.recv(64).decode()
            if self.validate_block(prev_block):
                connectionSocket.send(str.encode("200"))
                new_block = connectionSocket.recv(64).decode()
                self.insert_block(new_block)
            else:
                connectionSocket.send(str.encode("400"))

    def initalization(self):
        with open(self.blockchianFile,'r') as file_read:
            blocks = file_read.readlines()
            file_read.close()
        return len(blocks), blocks

    def validate_block(self, block):
        lastline = ""
        # Read last line
        # Not efficent for very large file
        with open(self.blockchianFile, 'r') as file_read:
            lines = file_read.read().splitlines()
            lastline = lines[-1]
            file_read.close()
        if lastline == block:
            print("Block Validated: ", block)
            return True
        else:
            print("Block Invalid: ", block)
            return False

    def insert_block(self, block):
        with open(self.blockchianFile, 'a') as file_append:
            file_append.write(block + "\n")
            file_append.close()
        print("New Block Added")

        
new_connection = TCPConnection()
new_connection.start()
