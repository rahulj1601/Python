import re

beginsWithHelloRegex = re.compile(r'^Hello') #string must begin with Hello
mo = beginsWithHelloRegex.search("Hello There!")
print(mo.group())

endsWithWorldRegex = re.compile(r'world!$') #string must end with world!

allDigitsRegex = re.compile(r'^\d+$') #must begin and end with at least 1 digit --> must be all digits

atRegex = re.compile(r'.at') #must be any single character followed by 'at' e.g. cat, hat, mat, sat
atRegex = re.compile(r'.{1,2}at') #must be any 1 or 2 characters followed by 'at' - can include spaces

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # .* finds the text in the place shown
# .* is always greedy
print(nameRegex.findall('First Name: Rahul Last Name: Jindal'))

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>') #Takes as little as possible within the angle brackets
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>') #Takes the most amount of text possible within the angle brackets
print(greedy.findall(serve))

prime = 'Serve the public trust. \nProtext the innocent. \nUpload the law.'
dotStar = re.compile(r'.*') #ignores the new line text
allDotStar = re.compile(r'.*', re.DOTALL) #the .* includes everything including the new line, match all and greedy match

mo = dotStar.search(prime)
print(mo.group())

vowelRegex = re.compile(r'[aeiou]', re.I) #re.I will tell the program to ignore case, match AEIOU and aeiou
