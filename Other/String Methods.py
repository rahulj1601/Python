spam = "Hello World!"
spam.upper() # Upper case
spam.lower() # Lower case
spam.title() # Makes it a title

# Returns boolean value - is it lower case / upper case
# Empty string returns false all the time
print(spam.islower())
print(spam.isupper())

# Joins the items in  a list with a specific character 
print(','.join(['cats','bats','rats']))
print('\n\n'.join(['cats','bats','rats']))

# Splits the items into list items
print("My name is Simon".split())
print("My name is Simon".split("m"))

# Adds spaces or characters to the string to move the item to the left or right and make it the desired length
print("Hello".rjust(10))
print("Hello".ljust(10))
print("Hello".rjust(20,'*'))

# Centers the text with the length 20 and = signs on either side
print("Hello".center(20, "="))

# Removes the whitespace from the string
spam = "Hello".rjust(10)
spam.strip()
spam.lstrip() # Remove whitespace from just the left of the string
spam.rstrip() # Remove whitespace from just the right of the string

# Strips the letters a,m,p,S from either side until none of those letters can be stripped
# Returns 'BaconSpamEgg'
'SpamSpamBaconSpamEggSpamSpam'.strip('ampS')

# Replaces all of the 'e' in spam with 'XYZ'
spam = "Hello there"
spam.replace('e', 'XYZ')




