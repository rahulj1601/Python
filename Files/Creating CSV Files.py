# Creating CSV Files

import csv

row = [1,2,3]

with open("Table.csv", mode="w") as myFile:
    writer = csv.writer(myFile)
    writer.writerow(row)

with open("Table.csv", mode="a") as myFile:
    writer = csv.writer(myFile)
    writer.writerow(row)
