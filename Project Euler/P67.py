with open("p67_pyramid.txt", mode="r") as myFile:
    temp = myFile.read()
temp = temp.split("\n")
print(temp)

temp = [[item] for item in temp]
pyramid = []

for i in range(0,len(temp)):
    pyramid.append(temp[i][0].split(" "))
    pyramid[i] = [int(j) for j in pyramid[i]]

for x in range(len(pyramid)-1,-1,-1):
    for y in range(0,len(pyramid[x])-1):
        if pyramid[x][y] > pyramid[x][y+1]:
            pyramid[x-1][y] += pyramid[x][y]
        else:
            pyramid[x-1][y] += pyramid[x][y+1]
    del pyramid[x]

    if len(pyramid) == 1:
        print(pyramid[0][0])
