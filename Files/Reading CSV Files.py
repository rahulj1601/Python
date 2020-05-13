# Reading CSV Files

import csv

with open("Table.csv", mode="r") as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        print(row)
