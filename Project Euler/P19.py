from datetime import date

firstSun = date(1900,12,30)
sunday = 0

for i in range(1901,2001):
    for j in range(1,13):
        difference = date(i,j,1) - firstSun
        if int(str(difference).split(" ")[0]) % 7 == 0:
            sunday += 1

print(sunday)
    
