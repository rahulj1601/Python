# CSV Formatting

import csv

people = [["Name","Age","Gender"],
          ["Spock","29","Male"],
          ["Dave","82","Male"],
          ["Maya","45","Female"]]

with open("People.csv",mode="w") as myFile:
    writer = csv.writer(myFile, delimiter = "|",lineterminator="\n\n",quotechar='"',quoting=csv.QUOTE_ALL)
    writer.writerows(people)
