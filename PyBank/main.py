"""Adeyemi Thomas Homework Assignment 2

"""

#Import pathlib and csv library
from pathlib import Path

import os
import csv


#Setting file path to budget_data.csv 
budget_data = Path('./Resources/budget_data.csv')


#Declare the variables/create lists
months = []
profits = []
profit_change = []


#Open the csv file 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip header row to avoid miscounting row data
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    #Read each row of data after the header
    for row in csvreader:
        #total months and net profit/loss
        months.append(row[0])
        profits.append(int(row[1]))
    
    #Calculate total number (length) of months
    total_months = len(months)
    
    #Calculate profit/loss change over the entire period
    for i in range(1, len(profits)):
        profit_change.append((int(profits[i]) - int(profits[i-1])))
    
    #Calculate average of profit/loss change
    profit_average = sum(profit_change) / len(profit_change)
    
    #Calculate greatest increase in profits 
    increase = max(profit_change)
    
    #Calculate greatest decrease in profits
    decrease = min(profit_change)


#Print results
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(total_months))
print("Net Total: $" + str(sum(profits)))
print("Average Change: $" + str(profit_average))
print()
print("Greatest Increase in Profits: " + str(months[profit_change. index(max(profit_change))+1]) + " ($" + str(increase) + ")")
print("Greatest Decrease in Profits: " + str(months[profit_change. index(min(profit_change))+1]) + " ($" + str(decrease) + ")")
print("----------------------------------------------------------")



#Export output to a text file for results
file = open("output.txt","w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------------------------------------" + "\n")
file.write("Total Months: " + str(total_months) + "\n")
file.write("Net Total: $" + str(sum(profits)) + "\n")
file.write("Average Change: $" + str(profit_average) + "\n")
file.write("Greatest Increase in Profits: " + str(months[profit_change. index(max(profit_change))+1]) + " ($" + str(increase) + ")" + "\n")
file.write("Greatest Decrease in Profits: " + str(months[profit_change. index(min(profit_change))+1]) + " ($" + str(decrease) + ")" + "\n")
file.write("----------------------------------------------------------" + "\n")
file.close()

