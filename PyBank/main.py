import os
import csv

#specify file to pull from:
budget_data = os.path.join("Resources", "budget_data.csv")

#Name Variables
Month=[]
Profit_Losses=[]
Change_PL=[]

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
    Change_PL.append(Profit_Losses[r+1]-Profit_Losses[r])

#Calculate the greatest increase in profits (date and amount) over the entire period
Max_Profit = max(Change_PL)
Max_Date = str(Month[Change_PL.index(max(Change_PL))+1])


#Calculate the greatest decrease in losses (date and amount) over the entire period
Min_Profit = min(Change_PL)
Min_Date = str(Month[Change_PL.index(min(Change_PL))+1])

print("Financial Analysis")
print("--------------------------------------------------")
print(f'The total number of months included in the dataset is {len(Month)}')
print(f'The net total amount of Profit & Losses over the entire period is $ {sum(Profit_Losses)}')
print(f'The average change is $ {round((total_profit_losses)/len(Month),2)}')
print(f'The Greatest Increase in Profits was: {Max_Date} ${Max_Profit}')
print(f'The Greatest Decrease in Profits was: {Min_Date} ${Min_Profit}')

output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "-----------------------------------------------"
line3 = str(f'The total number of months included in the dataset is: {str(Month)}')
line4 = str(f'The net total amount of Profit & Losses over the entire period is ${str(sum(Profit_Losses))}')
line5 = str(f'The average change is ${str(round((total_profit_losses)/len(Month),2))}')
line6 = str(f'The Greatest Increase in Profits was: {Max_Date} (${str(Max_Profit)})')
line7 = str(f'The Greatest Decrease in Profits was: {Min_Date} (${str(Min_Profit)})')
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))