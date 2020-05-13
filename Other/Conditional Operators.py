# Conditional Operators

x = 2
print(x == 2)
print(x != 2)

print(x < 3)
print(x > 3)

print(x <= 4)
print(x >= 4)

name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

nameList = ["John", "Rick", "Dave", "Gary"]
if name in nameList:
    print("Name is in the Name List!")

list1 = []
list2 = []
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)

print(not False)
print((not False) == (False))

    
    

