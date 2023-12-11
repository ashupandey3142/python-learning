marks = [12, 28, 38, 21, 45, 83, 72]

# Without enumerate
ind = 0
for mark in marks:
    print(mark)
    if ind == 3:
        print(f"index {ind} value is {mark}")
    ind+=1


# if we want to use index in easy way
# Enumerate function is a built-in function which allow you to loop over a seq
# and get index value of each element in the sequence at the same time
for v in enumerate(marks):
    print(v)

for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print(f"index {index} value is {mark}")

# enumerate map each value with the index number by default it start with 0
# but we can provide the starting number by providing second parameter of enumerate function

for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 3:
        print(f"index {index} value is {mark}")
# enumerate() is particularly useful in scenarios where you need both the index and the value of elements while iterating over a sequence.


fruits = ['apple', 'banana', 'cherry']
fruit_dict = {index: value for index, value in enumerate(fruits, start=1)}
print(fruit_dict)
