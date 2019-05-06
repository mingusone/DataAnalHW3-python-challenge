import os
import csv
csvPath = os.path.join("Resources","budget_data.csv")
reportPath = os.path.join("budget_report.txt")
# The total number of months included in the dataset
totalMonths = 0
# The net total amount of "Profit/Losses" over the entire period
totalProfits = 0.0
# The average of the changes in "Profit/Losses" over the entire period
sumOfChanges = 0.0
avgChange = 0.0
# The greatest increase in profits (date and amount) over the entire period
greatestInc = ["Mon-9999",0.0]

# The greatest decrease in losses (date and amount) over the entire period
greatestDec = ["Mon-9999",0.0]



with open(csvPath, newline="") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    next(csvReader) #for header

    previousPnL = 0.0 #previous profit and losses
    currPnL = 0.0 #the PnL we're working with in the for loop
    firstRow = True
    for row in csvReader:
        currPnL = float(row[1])
        totalMonths += 1 #add the total months
        totalProfits += currPnL #add the new money

        if firstRow:
            previousPnL = currPnL
            firstRow = False
            print("first row special")
            continue
    
        change = currPnL - previousPnL

        if change > greatestInc[1]:
            greatestInc[0] = row[0] #Get the mon&year of the row
            greatestInc[1] = change #slip in that change in profits
        elif change < greatestDec[1]:
            greatestDec[0] = row[0]
            greatestDec[1] = change

        sumOfChanges += change #add current delta to delta sum variable
        previousPnL = currPnL


    avgChange = round((sumOfChanges / (totalMonths-1)),2) #The first month has no change

    with open(reportPath, 'w', newline="") as reportFile:
        reportFile.write("Financial Analysis\n")

        reportFile.write("----------------------------\n")
        reportFile.write(f"Total Months: {totalMonths}\n")
        reportFile.write(f"Total: ${totalProfits}\n")
        reportFile.write(f"Average Change: ${avgChange}\n")
        reportFile.write(f"Greatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})\n")
        reportFile.write(f"Greatest Increase in Profits: {greatestDec[0]} (${greatestDec[1]})\n")
