<<<<<<< HEAD
#Analyzes the records to calculate each of the following:
#  * The total number of months included in the dataset
#  * The net total amount of "Profit/Losses" over the entire period
#  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period
#   Analysis should look similar to the one below:
#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```
#* In addition,  print the analysis to the terminal and export a text file with the results.


import os
import csv

csvpath = os.path.join('C:/Users/19134/Desktop/Homework/Python_Challenge/python-challenge/PyBank/Resources/budget_data.csv')

months = []
profit = []
profit_change = []

with open(csvpath) as pybank:

    # CSV reader specifies delimiter and variable that holds contents
    pybank = csv.reader(pybank, delimiter=',')
    #print(pybank)

    # Read the header row first 
    header = next(pybank)
    print(f"Header: {header}")
    
    # determine number of months
    months = len(list(pybank))
    print(months)

    def sum(profit):
         total = int(profit[1])
         print(sum(profit))

    # Read each row of data after the header
    for row in pybank:
        print(row)
# test commit change
=======
#Analyzes the records to calculate each of the following:
#  * The total number of months included in the dataset
#  * The net total amount of "Profit/Losses" over the entire period
#  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period
#   Analysis should look similar to the one below:
#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```
#* In addition,  print the analysis to the terminal and export a text file with the results.


import os
import csv

csvpath = os.path.join('C:/Users/19134/Desktop/Homework/Python_Challenge/python-challenge/PyBank/Resources/budget_data.csv')

months = []
profit = []
profit_change = []

with open(csvpath) as pybank:

    # CSV reader specifies delimiter and variable that holds contents
    pybank = csv.reader(pybank, delimiter=',')
    #print(pybank)

    # Read the header row first 
    header = next(pybank)
    print(f"Header: {header}")
    
    # determine number of months
    months = len(list(pybank))
    print(months)

    def sum(profit):
         total = int(profit[1])
         print(sum(profit))

    # Read each row of data after the header
    for row in pybank:
        print(row)

>>>>>>> 7cfa41a0cd32d32b3d4f3bec4c73023de8b56cdb
