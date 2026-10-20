import pickle
import hashlib
import hmac

# the only way to securely deserialize data is to always verify that the data wasn't tampered with. Always deserialize trusted data that didn't cross a trust boundary.

class MyUser(object):
    def __init__(self, name):
        self.name = name

# Secret Key provided to trusted apps. It should never be hardcoded, it is just mentioned here as a POC. 
KEY = b"secret"
# Signature Length also for POC
SIGNATURE_LENGTH = 32

serialized_filename="serialized.native"
#serialized_filename = "serialized.untrusted"

with open(serialized_filename, 'rb') as file_object:    
    raw_data = file_object.read()

try:
    # Check if raw data contains at least a signature
    if len(raw_data) > SIGNATURE_LENGTH:
        # Read signature part of raw data
        read_signature = raw_data[:SIGNATURE_LENGTH]
        # read the serialized part of raw data
        data = raw_data[SIGNATURE_LENGTH:]
        # Calculate and Compare Signatures
        computed_signature = hmac.new(KEY, data, hashlib.sha256).digest()  
        # don't compare with == as a hacker can get info about the signatures using timing attacks 
        # always use builtin comparison functionality, string comparison isn't cryptographically secure
        if hmac.compare_digest(read_signature, computed_signature):
            deserialized = pickle.loads(data)
            print(deserialized.name)
        else:
            print("Signature Mismatch")
except:
    print("Error occurred.")
