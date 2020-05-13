import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob"))
print(namesRegex.sub("REDACTED","Agent Alice gave the secret documents to Agent Bob"))
# Substitutes a string for the items found in the string

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r"Agent \1****", "Agent Alice gave the secret documents to Agent Bob"))
#\1 refers to group 1 inside the compile statement


re.compile(r'''
(\d\d\d)|     # area code
-          # first dash
\d\d\d     # first 3 digits
-          # second dash
\d\d\d\d   # last 4 digits''', re.VERBOSE)

# in verbose mode you can add comments and spaces that aren't actually part of the regular expression but make it more readable



re.compile(r'''
(\d\d\d)|     # area code
-          # first dash
\d\d\d     # first 3 digits
-          # second dash
\d\d\d\d   # last 4 digits''', re.VERBOSE | re.DOTALL | re.VERBOSE)

# to use various second arguments you use the bitwise OR operator aka pipe character to separate them
