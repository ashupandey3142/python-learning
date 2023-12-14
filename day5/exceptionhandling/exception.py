# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:


# Many Exceptions
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Unsupported operand type")
    except Exception as e:
        print(f"Error: {e}")


try:
    # Example 1: Division by zero
    print("----------Example 1: Division by zero------------")
    result1 = divide_numbers(5, 0)
except Exception as e:
    print(f"Exception caught: {e}")

try:
    # Example 2: Unsupported operand type
    print("---------Example 2: Unsupported operand type-------------")
    result2 = divide_numbers(10, "2")
except Exception as e:
    print(f"Exception caught: {e}")

try:
    # Example 3: Normal division
    print("-----------Example 3: Normal division-----------")
    result3 = divide_numbers(8, 2)
except Exception as e:
    print(f"Exception caught: {e}")
else:
    print(f"Result: {result3}")



# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except NameError as e:
    print(f"Something went wrong: {e.__str__()}")
finally:
    print("The 'try except' is finished")


# This can be useful to close objects and clean up resources:
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
