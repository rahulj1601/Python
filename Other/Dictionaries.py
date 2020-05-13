myCat = {'size': 'fat', 'colour': 'gray', 'disposition': 'loud'}

list(myCat.keys()) # Returns the keys which would be size, colour and disposition
list(myCat.values()) # Returns the values which would be fat, gray and loud

print(list(myCat.items()))
# Returns the items which would be 3 tuples of the items

for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

# Use two variables to refer to the keys and values
for k, v in myCat.items():
    print(k,v)

# Get the value attributed to size and if that doesn't exist return 0
# If nothing is placed where the 0 is then 'None' is returned if the key doesn't exist
print(myCat.get("size",0))

# If the colour key doesn't exist then the default value will be set as black
eggs = {"name":"Zophie", "species":"cat", "age":8}
eggs.setdefault("colour", "black")
# Orange will not be set as the colour because there is already a value for this key
eggs.setdefault("colour", "orange")




