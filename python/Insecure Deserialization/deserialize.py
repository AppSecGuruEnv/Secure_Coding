import pickle
import hashlib
import hmac

SIGNATURE_LENGTH = 32

class MyUser(object):
    def __init__(self, name):
        self.name = name

#serialized_filename="serialized.native"
serialized_filename = "serialized.untrusted"

with open(serialized_filename, 'rb') as file_object:
    raw_data = file_object.read()

# Try catch is a good practice and might protect against some corrupted serialized data. However it doesn't provide full protection, and with our serialized.untrusted data the execution will still occur as it is a valid serialized data which will be executed during unpickling before the error generation.
try:
    deserialized = pickle.loads(raw_data)
    # below assert function will stop the execution if the deserialized data doesn't match the object of MyUser but that will be too late. Execution will occur during the above step. 
    assert(isinstance(deserialized, MyUser))
    print(deserialized.name)
except:
    print("Error occurred.")
