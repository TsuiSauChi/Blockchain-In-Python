# Using Elliptic Curve Cryptography
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Hash import RIPEMD160
import base64
import sys

class Identity:
    def __init__(self):
        self.privateKey = ECC.generate(curve='P-256')
        self.publicKey = self.privateKey.public_key()
        self.address = self.generateAddress(self.publicKey)

    def generateAddress(self, public_key):
        # H = RIPEMD160(SHA256(Public_key))

        # Hashing Public Key with SHA256
        SHA256_payload = SHA256.new()
        SHA256_payload.update(str.encode(str(public_key)))
        SHA256_payload = SHA256_payload.hexdigest()

        # Hashing with RIPEMD160
        RIPE_payload = RIPEMD160.new()
        RIPE_payload.update(str.encode(SHA256_payload))
        RIPE_payload = RIPE_payload.hexdigest()

        # hashing payload twice with SHA256
        SHA256_checksum = SHA256.new()
        SHA256_checksum.update(str.encode(RIPE_payload))
        SHA256_2_checksum = SHA256.new()
        SHA256_2_checksum.update(str.encode(SHA256_checksum.hexdigest()))
        SHA256_2_checksum = SHA256_2_checksum.hexdigest()
        
        # concatenate payload with inital 4 bytes of checksum 
        # encoding using base64 due to the lack of base58 library
        address = RIPE_payload + SHA256_2_checksum[:32]
        address = address.encode("ascii")
        return base64.b64encode(address).decode()

    def getPrivateKey(self):
        return self.privateKey

    def getPublicKey(self):
        return self.publicKey

    def getAddress(self):
        return self.address
