# Writing a Dictionary to a CSV File

import csv

data = [{"Mountain":"Everest","Height":"8848"},
        {"Mountain":"K2","Height":"8611"},
        {"Mountain":"Kanchenjunga","Height":"8586"}]

with open("Peak.csv","w") as myFile:
    fields = ["Mountain","Height"]
    writer = csv.DictWriter(myFile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
