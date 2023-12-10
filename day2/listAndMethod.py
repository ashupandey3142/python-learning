# # Input
# n = input("Enter your name:")
# print(n)
# print(type(n))
#
#
# num = int(input("Python take input as string so after taking typecast into another data type depending upon requirements: "))
# print(num+3)
# print(type(num))

# List  and List method
a = ["hello", "how", "are", "you", "?"]
print(type(a))
print(a)

# Access
print(a[1])
print(a[1:])
print(a[3:4])
print(a[-2]) #negative indexing
print(a[:3])
print(a[-4:-1])


# Change Item Value
a[2] = ""
a.append("I am fine") # list are mutable
print(a)
a.append(1)
print(a)
a.append(2.111)
print(a)
a.remove("I am fine")
print(a)

print(a.count(1))
# a.index()

l1 = [2,5,1,2,3,4]
l1.sort()
print(l1)
l1.pop() # remove last element
l1.insert(2, 23)
print(l1)
l1.append([76, 65, 54])
l1.extend([22, 21, 29])
print(l1)


# Looping Using List Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)


#  Syntax
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in range(10)]
