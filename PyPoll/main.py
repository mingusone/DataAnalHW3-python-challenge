

import os
import csv

csvPath = os.path.join("Resources", "election_data.csv")
reportPath = os.path.join("election_report.txt")

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


# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

with open(reportPath, "w", newline = "") as reportFile:
    reportFile.write("Election Results\n")
    reportFile.write("-------------------------\n")
    reportFile.write(f"Total Votes: {totalVotes}\n")
    reportFile.write("-------------------------\n")
    
    #real quick break in the middle of writting to figure out the winner so we can mooch off this candidates for loop
    winner = ["name",0]
    for cd in candidates:

        #lets just find the winner real fast...
        if candidates[cd] > winner[1]:
            winner[0] = cd
            winner[1] = candidates[cd]

        #ok back to writting all the candidates, their votes, percentage...
        percentWin = (float(candidates[cd])/totalVotes)*100
        reportFile.write(f'{cd}: {"{:.3f}".format(percentWin)}% ({candidates[cd]})\n')
    
    
    reportFile.write("-------------------------\n")    
    reportFile.write(f"Winner: {winner[0]}\n")
    reportFile.write("-------------------------\n")    
