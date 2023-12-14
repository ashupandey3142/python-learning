# Dict and method
#  dictionary is a key value pair
dict1 = {}
print(type(dict1))
dict1 = {"hello": 1, "good": 2, "work": 1}


# Accessing Items
print(dict1.keys())
print(dict1.values())
print(dict1["hello"])
print(dict1.get("work"))


# Change Values
print(dict1.pop("hello"))
dict1["bad"] = 4
dict1["time"] = 12
print(dict1)
dict1.update({"color": "red"})



# Loop Through a Dictionary
for x in dict1:
    print(x)
for x in dict1.values():
    print(x)

for x in dict1.keys():
    print(x)

for key, value in dict1.items():
    print(f"{key} is related to {value}")


# Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)
l = ["a", "b", "c", "a", "d", "c"]
words = {x: l.count(x) for x in l}
print(words)


# print(dict1["something"]) #throws error
print(dict1.get("something")) # doesn't thorws error
#  get help in not getting error
