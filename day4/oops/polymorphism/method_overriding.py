class Shape:
    def __init__(self, color='black'):
        self.color = color

    def area(self):
        pass

    def display_info(self):
        print(f"Shape - Color: {self.color}, Area: {self.area()}")


class Circle(Shape):
    def __init__(self, radius, color='red'):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side_length, color='blue'):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length**2


class Triangle(Shape):
    def __init__(self, base, height, color='green'):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Create instances of different shapes
circle = Circle(radius=5)
square = Square(side_length=4)
triangle = Triangle(base=6, height=3)

# Display information about each shape
circle.display_info()
square.display_info()
triangle.display_info()
