import os
import csv

#specify file to pull from:
budget_data = os.path.join("Resources", "budget_data.csv")

#Name Lists
Month=[]
Profit_Losses=[]
Avg_Change=[]

#Open CSV
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        Month.append(row[0]) 
        Profit_Losses.append(int(row[1]))

#Calculate the total number of months included in the dataset
    total_months = len(Month)

#Calculate the net total amount of "Profit/Losses" over the entire period
    total_profit_losses=0
    for row in Profit_Losses:
        total_profit_losses = int(total_profit_losses) + int(row)

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
for r in range(len(Profit_Losses)-1):
    Avg_Change.append(Profit_Losses[r+1]-Profit_Losses[r])

def mean(changes):
    return sum(changes) / len(changes)

#Calculate the greatest increase in profits (date and amount) over the entire period
Max_Profit = max(Profit_Losses)
Max_Date = str(Month[Avg_Change.index(max(Avg_Change))+1])


#Calculate the greatest decrease in losses (date and amount) over the entire period
Min_Profit = min(Profit_Losses)
Min_Date = str(Month[Avg_Change.index(min(Avg_Change))+1])

print(f'The total number of months included in the dataset is {len(Month)}')
print(f'The net total amount of Profit & Losses over the entire preiod is $ {sum(Profit_Losses)}')
print(f'The average change is $ {round(sum(Avg_Change)/len(Avg_Change),2)}')