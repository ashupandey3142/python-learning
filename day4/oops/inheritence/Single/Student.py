from Basic.day4.oops.classesAndObjects.Person import Person


class Student(Person):
    def __init__(self, name, age, subject):
        self.subject = subject
        Person.__init__(self, name, age)
    #     Add Properties
        self.graduation_year = 2019

    def __str__(self):
        return f"{super().__str__()}(subject = {self.subject}, graduate in {self.graduation_year})"


x = Student("Mike", 21, "Math")
x.printname()
print(x)
