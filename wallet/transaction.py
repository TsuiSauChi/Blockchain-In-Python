# Cryptography Library: pycryptodome

# Using Elliptic Curve Cryptography
from Crypto.PublicKey import ECC
# Digital Signature Algorithm
from Crypto.Signature import DSS
# SHA256
from Crypto.Hash import SHA256

import random

# To be Added: Receiver and add cryptocurrency

class Transaction:
    def __init__(self, sender, transaction):
        self.transactionID = random.randrange(1000000, 9999999)
        self.transaction = str(transaction)
        self.sender = sender
        self.public_key = sender.getPublicKey()
        self.signature = None

    # Using Sender's private Key to encrypt
    def sign(self, privateKey):
        h = SHA256.new(self.transaction.encode())
        signer = DSS.new(privateKey, 'fips-186-3')
        self.signature = signer.sign(h)

    # Using Sender's public Key to verify transaction
    def verify(self):
        h = SHA256.new(self.transaction.encode())
        verifier = DSS.new(self.public_key, 'fips-186-3')
        try:
            verifier.verify(h, self.signature)
            return True
        except ValueError:
            return False

    def getSignature(self):
        return self.signature

