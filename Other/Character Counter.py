import pprint
# Pretty print module to make it look far nicer

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
# We will show how many times a specific character appears in the message

for char in message.upper():
    count.setdefault(char,0)
    count[char] += 1

# If you wanted to hold the formatted text in a variable
text = pprint.pformat(count)
print(text)

pprint.pprint(count)
