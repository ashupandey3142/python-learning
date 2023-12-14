
# Garbage collection in Python is the process of automatically identifying and reclaiming memory that is no longer in use by the program.

import gc


class MyClass:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} created')


print(gc.get_count())

# creating circular reference -> sometime in complex program and circular reference prevents the automatic garbage collection
obj1 = MyClass('Object 1')
print(gc.get_count())
obj2 = MyClass('Object 2')
obj1.ref = obj2
obj2.ref = obj1
print(gc.get_count())

# Delete references to break the circular reference
del obj1, obj2

# Force garbage collection
gc.collect()

print(gc.get_count())
print('Garbage collection done')
