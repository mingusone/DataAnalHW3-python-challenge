import os
import csv

csvPath = os.path.join("Resource", "election_data.csv")

with open(csvPath,newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")