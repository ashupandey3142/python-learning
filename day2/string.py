# String and String method
name = "Ashu"
print(name)
name = 'Ashu'
print(name)
print(name[0:2]) # start from 0  and go to 1
print(name[1:3])
print(name.count('s'))

for x in name:
    print(x.upper())
a = "abcd*"
print("a", a.isalnum()) #check special character is present or not if present then return false else true
b = "6"
print("b", b.isnumeric()) #check string is number or not
print(name.isnumeric())

print(name.find('s'))
print(name.replace('s', 'b'))
# strings are immutable
# name[0] = 's' # -> throws error
