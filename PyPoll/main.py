

import os
import csv

csvPath = os.path.join("Resources", "election_data.csv")

# The total number of votes cast
totalVotes = 0

# A complete list of candidates who received votes
candidates = {}

# The percentage of votes each candidate won
#for candidate in candidates...

# The total number of votes each candidate won
#look at candidates dict

# The winner of the election based on popular vote.

with open(csvPath,newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    next(csvReader) #header stuff
    for row in csvReader:
        candidate = row[2]
        totalVotes += 1
        try:
            candidates[candidate]
        except:
            candidates[candidate] = 0
        
        candidates[candidate] = candidates[candidate] + 1

    print(candidates)

        # try:
        #     pieShoppingBag[pieSelection[pieChoice-1]]
        #     print("we got an error! But we really shouldn't since we mapped it out up top :X")
        # except:
        #     pieShoppingBag[pieSelection[pieChoice-1]] = 0
