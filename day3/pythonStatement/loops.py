for i in range(6):
    if i == 3:
        continue
    print(i+1)

item = {"Banana", "Apple", "default"}
for i in item:
    print(i)

# ideally range will increment value by 1, but we can change the increment value by adding 3rd parameter
for x in range(2, 20, 3):
    print(x)


# else block can be used with for loop, if for loop runs completely then else block going to be executed
for x in range(6):
    # if x == 3: break #else block will not going to executed if break statement is used in between
    print(x)
else:
    print("Finally finished!")



# list iteration
l = [2,4,1,4,6,7]
i=0
while(i<len(l)):
    print(l[i])
    i+=1


while(True):
    print("By entering 0 we you stop the program ")
    n=int((input("Enter number")))
    print(n)
    if n == 0:
        print("Program stopped")
        break

