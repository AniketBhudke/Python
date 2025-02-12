# Writing to JSON: Use json.dump() to write Python data to a JSON file.
import json

# Data to be written to the JSON file (Python dictionary)
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "languages": ["English", "Spanish"]
}

# Writing the dictionary to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully!")


# Reading from JSON: Use json.load() to read data from a JSON file into Python.

import json

# Reading the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Accessing the data
print("Data read from JSON file:")
print(data)
print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(f"City: {data['city']}")
print(f"Languages: {data['languages']}")

# Working with JSON strings: Use json.dumps() to convert Python data to a JSON string, and json.loads() to convert a JSON string back to Python.

import json

# Data to be converted to JSON string
data = {
    "name": "Bob",
    "age": 30,
    "city": "Chicago"
}

# Converting to a JSON string
json_string = json.dumps(data, indent=4)
print("JSON string:")
print(json_string)


import json

# JSON string
json_string = '{"name": "Bob", "age": 30, "city": "Chicago"}'

# Converting JSON string to Python data (dictionary)
data = json.loads(json_string)

print("Python dictionary:")
print(data)


# Writing to JSON: Convert a NumPy array to a Python list using tolist() and then use json.dump() to write it to a JSON file.
import numpy as np
import json

# Create a NumPy array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Convert NumPy array to a list (JSON can only serialize lists, not NumPy arrays)
data_list = data.tolist()

# Write the list to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

print("NumPy array successfully written to JSON file!")



# Reading from JSON: Load the JSON data using json.load(), and convert the list back to a NumPy array using np.array().

import numpy as np
import json

# Read the JSON file
with open('data.json', 'r') as json_file:
    data_list = json.load(json_file)

# Convert the list back to a NumPy array
data_array = np.array(data_list)

print("Data read from JSON file:")
print(data_array)
