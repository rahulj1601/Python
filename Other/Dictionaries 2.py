# Dictionaries

phonebook = {
    'John': 993298329,
    'Dave': 372937299,
    'Gary': 327932932
}

print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" %(name, number))

phonebook.pop("John")
print(phonebook)
    
