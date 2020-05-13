import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # creates a regex object
mo = phoneNumRegex.search(message) # creates a match object
print(mo.group()) # gets the matched string
print(mo.group(1)) # returns the first group defined by the parenthesis
print(mo.group(2)) # returns the second group defined by the parenthesis

print(phoneNumRegex.findall(message)) # finds all of the text following the same layout

# /d refers to a digit
# r'' --> raw string
