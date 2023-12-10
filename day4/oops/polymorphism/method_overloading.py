class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c


# Create an instance of the Calculator class
calc = Calculator()

result1 = calc.add(5)
result2 = calc.add(3, 7)
result3 = calc.add(2, 4, 6)

print(result1)
print(result2)
print(result3)
