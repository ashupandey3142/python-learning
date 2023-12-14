
try:
    f = open("filehandling.txt", "rt")
    #  r for read and t for text form
    print(f.read())

    # Read Only Parts of the File
    print("------------Read Only Parts of the File--------------")
    # By default the read() method returns the whole text, but you can also specify how many characters you want to return:
    print(f.read(50))

    # Read Lines
    # return one line by using the readline() method:
    print(f.readline())
    print(f.readline()) # By calling readline() two times, you can read the two first lines
    print(f.readline())
except Exception:
    print("rr")
finally:
    # Close Files
    f.close()
