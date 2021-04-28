# Using Elliptic Curve Cryptography
from Crypto.PublicKey import ECC

class Identity:
    def __init__(self):
        self.privateKey = ECC.generate(curve='P-256')
        self.publicKey = self.privateKey.public_key()

    def getPrivateKey(self):
        return self.privateKey

    def getPublicKey(self):
        return self.publicKey