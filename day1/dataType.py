# Data Type
# a data type defines the type of data that a variable can hold.


# Primitive Data type
# Numeric Types:	int, float, complex
x = 20
print(type(x))
x = 20.5
x = 1j
print(type(x))

# Boolean Type:	bool
x = True
print(type(x))


# Non Primitive
# Sequence Types:	list, tuple, range
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
x = range(6)
print(type(x))

# Text Type:	str
x = "Hello World"
print(type(x))

# Mapping Type:	dict
x = {"name" : "John", "age" : 36}
print(type(x))

# Set Types:	set, frozenset
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})

print(type(x))

# None Type:	NoneType
x = None
print(type(x))


# Typecasting
x="5"
print(int(x)+1)
