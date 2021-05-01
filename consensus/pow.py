# Simulation of Proof Of Work Protocol

from block import Block
import hashlib

# Function to solve math puzzle; find a SHA256 hash key depending on the difficulty set
def pow(key, difficulty):
    dif_list = [0] * difficulty
    dif_str = "".join(str(x) for x in dif_list)

    nonceValue = 0
    hash_value = hashlib.sha256(str.encode(key + str(nonceValue))).hexdigest()
    check = list()
    for i in hash_value[:difficulty]:
        check.append(i)
    check_str = "".join(str(x) for x in check)
    
    while dif_str != check_str:
        nonceValue += 1
        hash_value = hashlib.sha256(str.encode(key +  str(nonceValue))).hexdigest()
        check = list()
        for i in hash_value[:difficulty]:
            check.append(i)
        check_str = "".join(str(x) for x in check)

    print("Nonce value is:" ,nonceValue)
    print("Hash value is:", hash_value)
    return nonceValue

# Check whether the new block key matches the pow protocol
def check(hash_value, difficulty):
    dif_list = [0] * difficulty
    dif_str = "".join(str(x) for x in dif_list)

    check = list()
    for i in hash_value[:difficulty]:
        check.append(i)
    check_str = "".join(str(x) for x in check)

    if dif_str == check_str:
        return True
    else:
        return False
