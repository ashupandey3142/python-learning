
# Encapsulation is a way to restrict the direct access to some components of an object

class Base:
    def __init__(self):
        self.a = "Ashu"
        self.__c = "private variable"

    def get_c(self):
        return self.__c

    def set_c(self, new_c):
        self.__c = new_c


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        # Accessing private variable using getter
        # print(self.get_c())

        # Uncommenting the line below will raise an AttributeError
        # because __c is a private variable.
        print(self.__c)


obj1 = Base()
print(obj1.a)

# print(obj1.__c)
# Uncommenting print(obj1.c) will
# raise an AttributeError

obj2 = Derived()
obj2.set_c(21)
print(obj2.get_c())
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
