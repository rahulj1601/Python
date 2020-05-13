import re

batRegex = re.compile(r'Bat(wo)?man') # wo can appear 0 or 1 time --> use (...)?
mo = batRegex.search("The Adventures of Batman")
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man') # wo can appear 0 or more times --> use (...)*
mo = batRegex.search("The Adventures of Batwowowowoman")
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man') # wo can appear 1 or more times --> use (...)+
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())

haRegex = re.compile(r'(Ha){3}') # Use {n} where n is the number of times the object is found
mo = haRegex.search("He said 'HaHaHa'")
print(mo.group())

haRegex = re.compile(r'(Ha){3,5}') # Use {x,y} must match at least x times or at most y times inclusive
# x=blank space --> from 0 to y
# y=blank space --> from x to infinity
mo = haRegex.search("He said 'HaHaHaHaHa'")
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group()) # greedy match --> outputs first 5 numbers to find maximum length string

digitRegex = re.compile(r'(\d){3,5}?') # non greedy match --> outputs smallest possible string
mo = digitRegex.search('1234567890')
print(mo.group())

