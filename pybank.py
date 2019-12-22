import os
#importing module for reading CSV
import csv

#current working directory
curr_dir = os.getcwd()

filepath = os.path.join( curr_dir,'Resources','budget_data.csv')

#init variables
monthcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0

#open/read CSV
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
         #tracking greatest increase in profits
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #tracking decrease in profits
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Get total months (financial analysis)
         monthcount = monthcount + 1
         total += int(Amount) 
   
#The total number of months incld in dataset
print(f'Total Months : {monthcount}')

#total net amount of "Profit/Losses" over entire period
print(f'Total: $ {total}')

#greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')

#greatest decrease in profit
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')
