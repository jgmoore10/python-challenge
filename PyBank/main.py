import os
import csv

#specify file to pull from:
budget_data = os.path.join("Resources", "budget_data.csv")

#Open CSV
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Calculate the total number of months included in the dataset
total_months = budget_data.count() 

print(total_months)


#Calculate the net total amount of "Profit/Losses" over the entire period



#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#Calculate the greatest increase in profits (date and amount) over the entire period


#Calculate the greatest decrease in losses (date and amount) over the entire period