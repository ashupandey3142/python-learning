# Set and it's method
#  set is a collection of well-defined objects
# set is an unordered list
# duplicates are not allowed
s = { 5, 2, 3, 4, 2}
print(s)
s2 = { 1,2 ,3,4}
print(s == s2)

# Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Add Items and remove
print(s.pop()) # in set pop remove any random element, set is mutable
s.add(21)
print(s)
thisset.remove("banana")
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

s3 = {21, 22, 23}
s4 = s.union(s3)

print(s4)
print(s.intersection(s3))
print(type(s))
# empty set
b=set()
print(type(b))

for i in s4:
    print(i) # unordered
