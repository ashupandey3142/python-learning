
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading the addition operator
    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __str__(self):
        return f"{self.real} + {self.imag}j"


num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

# Use the overloaded addition operator
result = num1 + num2

# Display the result
print(result)  # Output: 4 + 6j
