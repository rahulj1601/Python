import re

message = "..."
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # All of the phone numbers following this pattern will be found
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))') # The phone numbers found will be placed in a tuple inside a list with the (phone number first, group1, group2)
phoneRegex.findall(message)

digitRegex = re.compile(r'\d') #all digits

vowelRegex = re.compile(r'[aeiouAEIOU]') #all vowels
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}') #2 vowels in a row
x = re.compile(r'[a-z]') #get all lower case letters

notVowelRegex = re.compile(r'[^aeiouAEIOU]') #match all non vowels (^ is called a carret)
