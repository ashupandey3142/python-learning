# staticmethod is used when a method doesn't access or modify the class or instance state.
# classmethod is used when a method needs access to the class itself, often for operations involving class-level variables.

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Using staticmethod without creating an instance
result_add = MathOperations.add(5, 3)
result_subtract = MathOperations.subtract(8, 4)

print("Result of addition:", result_add)
print("Result of subtraction:", result_subtract)
