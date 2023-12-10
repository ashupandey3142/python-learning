# Decorator 1
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("uppercase decorator", result)
        return result.upper()
    return wrapper


# Decorator 2
def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("exclamation decorator", result)
        return result + '!'
    return wrapper


@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

# Calling the decorated function
result = greet("John")
print(result)
