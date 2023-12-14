class Base:
    # Constructor
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Base):
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def get_age(self):
        return self.age


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


g = GrandChild("Geek1", 23, "Noida")
print(g.get_name(), g.get_age(), g.get_address())
