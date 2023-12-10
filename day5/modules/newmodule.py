# Re-naming a Module
import mymodule as mx
from mymodule import sum

mx.greeting("Jonathan")

# Variables in Module
a = mx.person1["age"]
print(a)

print(mx.prod(21,21))

s = sum(21,23)
print("sum", s)
