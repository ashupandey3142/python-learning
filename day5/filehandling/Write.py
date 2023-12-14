class Write:
    try:
        # "a" - Append - will append to the end of the file
        #
        # "w" - Write - will overwrite any existing content
        f = open("filehandling.txt", "at")
        try:
            f.write("Now the file has more content!")
            f.close()

            #open and read the file after the appending:
            f = open("filehandling.txt", "r")
            print(f.read())
            f.close()

            # f = open("filehandling.txt", "w")
            #
            # f.write("Woops! I have deleted the content!")
            # f.close()
            # #open and read the file after the overwriting:
            # f = open("filehandling.txt", "r")
            # print(f.read())
        except Exception as e:
            print(e.__str__())
        finally:
            f.close()
    except:
        print("file not found")
