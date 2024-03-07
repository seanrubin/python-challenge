#Importing Dependencies
import os
import csv
from pathlib import Path

#Declaring File Location
input_file = Path("..", "..", "python-challenge", "Pybank", "Resources", "budget_data.csv")

#Creating Empty Lists to Iterate Through Specified Rows for the Following Variables
total_months = []
total_profit = []
monthly_change = []

#Opening CSV in read mode
with open(input_file,newline="", encoding="utf-8") as budget:

    #Storing the Contents of the CSV into the Following Variable
    csv_budget = csv.reader(budget,delimiter=",")

    #Skipping the Header Labels
    header = next(csv_budget)

    #Iterate Through the Rows of the CSV
    for row in csv_budget:

        #Appending the Total Months and Total Profits
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Iterating Through the Profits to Get the Monthly Change in the Profits
    for i in range(len(total_profit)-1):

        #Taking the Difference Between Two Months and Appending to Monthly Change
        monthly_change.append(total_profit[i+1]-total_profit[i])

#Getting Max and Min of the Monthly Change
increase = max(monthly_change)
decrease = min(monthly_change)

#Correlating to the Proper Month
increase_monthly = monthly_change.index(max(monthly_change))+1
decrease_monthly = monthly_change.index(min(monthly_change))+1

#Printing Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[increase_monthly]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[decrease_monthly]} (${(str(decrease))})")

#Setting Up the Output File for the Analysis
output_file = Path("..", "..", "python-challenge", "Pybank", "Analysis", "Financial Analysis.txt")

with open(output_file, "w") as file:

    #Writing the Results to the Financial Analysis Text Document
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[increase_monthly]} (${(str(increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[decrease_monthly]} (${(str(decrease))})")