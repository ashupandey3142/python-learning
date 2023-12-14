if(8 < 9):
    print("8 less than 9")


a = [1,3,2,1,3]
count = 0
for i in a:
    if(i>2):
        count+=1
print("value greater than 2 are ", count)

# Q) Given an integer, n , perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird


n=int(input("Enter n:"))
if(n%2 != 0):
    print("Weird")
else:
    if (n >= 2 and n<5):
        print("Not Weird")
    elif (n >= 6 and n<=20):
        print("Weird")
    else:
        print("Not Weird")

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for
# the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#
# In the Gregorian calendar, three conditions are used to identify leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

year = int(input("Enter Year:"))
if((year % 400 == 0 and year % 100 == 0) or (year % 4 ==0 and year % 100 != 0)):
    print(year, " is leap year")
else:
    print(year, " is not a leap year")
