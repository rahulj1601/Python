helloFile = open('/Users/rahul/Documents/Programming/Automating the Boring Stuff with Python /Files/hello.txt')
content = helloFile.read() # reads the plaintext file
print(content)

helloFile.close() # closes the file after being used

helloFile = open('/Users/rahul/Documents/Programming/Automating the Boring Stuff with Python /Files/hello.txt')
helloFile.readlines() # reads the lines of the file and present them within a list

helloFile = open('/Users/rahul/Documents/Programming/Automating the Boring Stuff with Python /Files/hello2.txt', 'w') # write mode
# 'a' for append mode where you add to the end of the file contents

helloFile.write('Hello!!!!')
helloFile.close() # must close for the contents to be written to the file

### The Shelve Module

import shelve
shelfFile = shelve.open('mydata') #creates a binary file
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
