import os
import csv

#Path to collect data from the Resources Folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Store header row
    header = next(csv_reader)
    
    #Initialise month total
    month_total = 0

    #Initialise net profil/loss
    net_profit_loss = 0
    
    #define variables
    values_list = []
    profit_loss_change = []
    firstline = True
    date = []

    #loop through budget data csv
    for row in csv_reader:
        
        #Count of month
        month_total = month_total + 1

        #add profit/loss column to list
        values_list.append(float(row[1]))

        #add dates to date list
        date.append(str(row[0]))

        #Find monthly profit difference and add it to list
        if firstline == True:
            difference = float(row[1])
            firstline = False
        
        else:
            profit_loss_change.append(float(row[1]) - difference)
            difference = float(row[1])
            sum_change = sum(profit_loss_change)

    #average profit change               
    average_change = sum_change / (len(profit_loss_change))    
   
    
    #sum to get net profit loss
    net_profit_loss = sum(values_list)

    #find greatest profit and loss from monthly profit difference list
    greatest_profit = max(profit_loss_change)
    greatest_loss = min(profit_loss_change)

    #Find correspoinding date of greatest profit and loss
    greatest_increase_date_index = profit_loss_change.index(greatest_profit) + 1
    greatest_increase_date = date[greatest_increase_date_index]

    greatest_decrease_date_index = profit_loss_change.index(greatest_loss) + 1
    greatest_decrease_date = date[greatest_decrease_date_index]

    
#Print values in Git Bash
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {month_total}')
print(f'Total: ${net_profit_loss}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_profit})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_loss})')

#Output to new CSV file
output_path = os.path.join("analysis", "analysis.csv")

with open(output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerow([f"Total Months: {month_total}"])
    csvwriter.writerow([f"Total: ${net_profit_loss}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_profit})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_loss})"])