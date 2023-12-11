import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# convert to json
print(json.dumps(x))

print()
# Format the Result
print(json.dumps(x, indent=4))

# You can also define the separators, default value is (", ", ": "),
# which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Order the Result
print(json.dumps(x, indent=4, sort_keys=True))
