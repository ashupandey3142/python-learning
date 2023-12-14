# A simple generator for Fibonacci Numbers
def fib(limit):

    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b


x = fib(7)

print("Fibonacci Series:")
for i in x:
    print(i)
