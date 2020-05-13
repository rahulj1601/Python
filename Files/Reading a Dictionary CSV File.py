# Reading a Dictionary CSV File

import csv

with open("Peak.csv",mode="r") as myFile:
    reader = csv.DictReader(myFile)
    line = 1
    for row in reader:
        if line == 1:
            print(f'{", ".join(row)}')
            line+=1
        print(f'{row["Mountain"]},{row["Height"]}')
