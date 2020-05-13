with open("myFile.txt", mode = "w") as myFile:
    for each in range(1,11):
        myFile.write(str(each)+"\n")

with open("myFile.txt", mode="a") as myFile:
    for each in range(11,21):
        myFile.write(str(each)+"\n")


