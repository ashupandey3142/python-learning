
# Tuple and method
# Tuple is immutable
t1 = (2, 3, 4, 6, 4, 1)
print(t1.count(4))
print(t1.index(4))
# t1[0] = 12 # -> throws error as tuple is immutable

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# Change Tuple Values
y = list(thistuple)
y[1] = "kiwi"
x = tuple(y)

print(x)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
