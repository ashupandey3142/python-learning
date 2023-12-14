# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
#
# "x" - Create - will create a file, returns an error if the file exist
#
# "a" - Append - will create a file if the specified file does not exist
#
# "w" - Write - will create a file if the specified file does not exist
import os
class CreateAndDelete:
    try:
        f = open("demofile.txt","x")
        f.write("New file is created")
        # f.read() # throw error not readable
        f.close()

        #Delete file
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")
        else:
            print("The file does not exist")


    except Exception as e:
        print(e.__str__())
