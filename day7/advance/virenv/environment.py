# What is it?
# A virtual environment in Python is a self-contained directory that contains a Python interpreter and its standard library, as well as additional packages
# and modules. It allows you to create an isolated environment for your Python projects, with its own set of dependencies, without affecting the system-wide
# Python installation.
#
# Why use it?
# Imagine you're working on two different projects, and they need different versions of the same library. A virtual environment helps you keep them separate.
# It prevents conflicts and confusion between different projects.

import pandas as p
import requests
print(p.__version__)

# pip freeze -> will give us the list of installed module with version
# and if you want to put it in text file then run
# pip freeze > requirement.txt

# you can switch the environment and run command
# pip install -r requirements.txt
# this will install all the modules into the new virtual environment that are list inside text file

def fetch_data():
    url = 'https://dummyjson.com/products'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Fetched data:")
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_data()
