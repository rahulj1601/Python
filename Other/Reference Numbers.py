spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = "hello!"
print(cheese)
print(spam)
# This also changes spam[1] to "hello!"
# Because the variable name cheese will obtain the reference to the list spam
# So changing the list stored at that reference will also alter spam
# Because spam and cheese are connected to the same reference

# Immutable values don't experience these problems
# Because they can't be changed and can only be replaced by new values
