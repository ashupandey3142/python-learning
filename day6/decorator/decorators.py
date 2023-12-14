# Decorator is a function which takes argument as a function
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
# Decorator is used when we want without overriding existing function we can add some additional things, for e.g. authorization, logging and debugging

def greet(func):

    def modified_func():
        print("Good morning")
        func()
        print("Thanks for using this func")
    return modified_func

@greet
def hello():
    print("Hello world")

# greet(hello)() # Either we write this thing many time or instead of it we add @function_name and simply call that function as i have called below
hello()


# Decorator function for logging
def log_function_call(func):
    def wrapper(*args):
        print(f"Calling function {func.__name__} with arguments {args}")
        result = func(*args)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper


# Applying the decorator to a function
@log_function_call
def calculate_sum(a, b):
    return a + b


@log_function_call
def calculate_mul(a, b):
    return a * b


# Calling the decorated function
ans = calculate_sum(3, 5)
res = calculate_mul(4, 8)
# This can be useful for debugging, profiling, or monitoring the behavior of functions in a program without modifying their actual implementation
