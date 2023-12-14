# The with statement in Python is used to simplify the management of resources, such as files or network connections.
# It ensures that a setup code is executed before the block of code, and a cleanup code is executed afterward, even if an exception is raised during the execution.
# It helps in writing cleaner and more readable code for resource management.
# If an exception occurs within the with block, the __exit__ method of the context manager is still called, providing an opportunity for cleanup.


import os
# Step 1: Create a file and write something to it
file_path = 'example_file.txt'

with open(file_path, 'w') as file:
    file.write('Hello, this is an example file!\n')
    file.write('We are writing some content to test file operations.')
# File is automatically closed when exiting the 'with' block

# Step 2: Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()
    print("File Content:\n", file_content)

# Step 3: Delete the file

try:
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred while deleting the file: {e}")
