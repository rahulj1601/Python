import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # use pipe character to match one of many possible groups
mo = batRegex.search("Batmobile has lost a wheel")

print(mo.group())
print(mo.group(1)) # returns the second word found in the parenthesis
