# pickle is a module in Python that allows you to serialize and deserialize Python objects. Serialization is the process of converting
# a Python object into a byte stream,and deserialization is the reverse process, where you convert a byte stream back into a Python object.
# json is a better choice for data exchange between systems, while pickle is more suitable for Python-specific
# use cases where you need to serialize/deserialize Python objects within the same environment.
import pickle

# Data to be serialized
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Example City',
    'interests': ['programming', 'reading', 'traveling'],
    'Cache Mechanism': 'Caching results of expensive function calls. Instead of recalculating results, you can cache the output of a function to a file using pickle and retrieve it when needed'
}

# Serialize (Save to a file)
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize (Load from the file)
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# Print the loaded data
print("Loaded Data:")
print(loaded_data)

# Security Concerns: Be aware that pickle can execute arbitrary code(generated at run time) during deserialization, making it a potential security risk.
# Avoid unpickling data from untrusted or unauthenticated sources.
#
# Supported Types: Know which Python types can be pickled and which cannot. For example, file objects and certain types of functions may not be picklable.
# Version Compatibility: Be mindful of version compatibility when exchanging pickled data between different Python versions.

# Serialize an object to a byte string
# if you have pickled data in the form of a string or bytes, use loads. If you have a file containing pickled data, use load.

original_data = {'example_key': 'example_value'}
serialized_data = pickle.dumps(original_data)

# Deserialize the byte string back into a Python object
loaded_data = pickle.loads(serialized_data)

# Print the loaded data
print("Loaded Data:")
print(loaded_data)
