import pickle
import hashlib
import hmac

# the only way to securely deserialize data is to always verify that the data wasn't tampered with. Always deserialize trusted data that didn't cross a trust boundary.

class MyUser(object):
    def __init__(self, name):
        self.name = name

# Secret Key provided to trusted apps. It should never be hardcoded, it is just mentioned here as a POC. 
KEY = b"secret"

user = MyUser("Peter")
serialized = pickle.dumps(user)
# Calculate signature over serialized data
signature = hmac.new(KEY, serialized, hashlib.sha256).digest() # digest to store the value
#Calculate length of signature (constant), because we will need to calculate the signature part as well as the deserialization part later on.
SIGNATURE_LENGTH = len(signature) # 32 also just for POC
filename = "serialized.native"

with open(filename, 'wb') as file_object:
    # Write signature plus serialized data
    file_object.write(signature + serialized)

