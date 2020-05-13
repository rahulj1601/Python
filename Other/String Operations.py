# String Operations

astring = "Hello world!"

stringLen = len(astring)
print(stringLen)

indexNum = astring.index("o")
print(indexNum)

print(astring.count("l"))
print(astring[3:7])
print(astring[-3:-1])

alpha = "abcdefghijklmno"
print(alpha[3:9:2])

print(astring[::-1])
print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello"))
print(astring.endswith("hdhadaakhjdhsjhskj"))

testStr = "a,b,c,d,e,f"
words = testStr.split(",")
print(words)

