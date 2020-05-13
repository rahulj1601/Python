f = open('helloworld.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

myFile = open('helloworld.html', 'r')
newFile = open('newFile.html','w')

for each in myFile:
    newFile.write(each)
    
newFile.close()
myFile.close()
