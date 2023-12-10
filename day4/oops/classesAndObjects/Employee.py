class Employee:
    # Class, Static and Instance Variables
    # Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances
    # of the class. Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables
    # are variables whose value is assigned in the class.

    # Class Variable
    category = "general"
    def __init__(self, name, salary):
        # Instance variable
        self.name = name
        self.salary = salary

    # Calling destructor
    def __del__(self):
        print("Destructor called")

    def get_salary(self):
        return self.salary
    @staticmethod
    def get_max_value(x, y):
        return max(x, y)

rohan = Employee("Rohan", "24000")
print(rohan.get_salary())
print(rohan.name)
print(Employee.category)
# print(Employee.name)
print(rohan.get_max_value(10,20))
print(Employee.get_max_value(20,10))
