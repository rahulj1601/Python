alphaScore = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,
              "K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,
              "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

with open("p022_names.txt", "r") as myFile:
    names = myFile.read()

names = sorted((names.replace('"',"")).split(","))
totalScore = 0

for i in range(1,len(names)+1):
    nameScore = 0
    for char in names[i-1]:
        nameScore += alphaScore[char]
    nameScore *= i
    totalScore += nameScore

print(totalScore)
        
    
