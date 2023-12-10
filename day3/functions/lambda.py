# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
from functools import reduce
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


x = lambda a: a*a

print(x(21))
# lambda function is used as callback function
# it is used in map, filter, reduce

num = [1,2,3,4,5,6,7,8]

even = list(filter(lambda a: a % 2 == 0, num))
print(even)

print(list(map(lambda n: n*2, even)))

sum = reduce(lambda a,b: a+b, even)
print(sum)
