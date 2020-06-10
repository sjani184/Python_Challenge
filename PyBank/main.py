
import os
import csv

input_path = os.path.join('.' , 'PyBank', 'Resources', 'budget_data.csv')

Total_Months = 0 
Total_Profit  = 0 
Average_Change = 0
Profit_Change = []
Change_Month = []
Largest_Inc = 0 
Largest_Inc_Month = 0
Largest_Dec = 0
Largest_Dec_Month = 0

with open(input_path, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    row = next(csvreader)

    previous_profit = int(row[1])
    Total_Months += 1
    Total_Profit += int(row[1])
    Largest_Inc = int(row[1])
    Largest_Inc_Month = row[0]

    for row in csvreader:

        Total_Months += 1 
        Total_Profit += int(row[1])

        Profit_Changes = int(row[1]) - previous_profit
        Profit_Change.append(Profit_Changes)
        previous_profit = int(row[1])
        
        if int(row[1]) > Largest_Inc:
            Largest_Inc = int(row[1])
            Largest_Inc_Month = (row[0])

        if int(row[1]) < Largest_Dec:
            Largest_Dec = int(row[1])
            Largest_Dec_Month = (row[0])

    high = max(Profit_Change)
    low = min(Profit_Change)


    Average_Change = sum(Profit_Change) / len(Profit_Change)


output_path = os.path.join('.', 'Pybank', 'Analysis', 'PyBank_Analysis.text')

with open(output_path, 'w',) as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write('\n' + "----------------------------")
    txtfile.write('\n' + "Total Months: " + str(Total_Months) )
    txtfile.write('\n' + "Total: " + "$" + str(Total_Profit))
    txtfile.write('\n' + "Average Change: " + "$" + str(Average_Change))
    txtfile.write('\n' + "Greatest Increase in Profits: " + str(Largest_Inc_Month + " $" + str(high)))
    txtfile.write('\n' + "Greatest Decrease in Profits: " + str(Largest_Dec_Month + " $" + str(low)))
   
print("Financial Analysis")
print('\n' + "----------------------------")
print('\n' + "Total Months: " + str(Total_Months) )
print('\n' + "Total: " + "$" + str(Total_Profit))
print('\n' + "Average Change: " + "$" + str(Average_Change))
print('\n' + "Greatest Increase in Profits: " + str(Largest_Inc_Month + " $" + str(high)))
print('\n' + "Greatest Decrease in Profits: " + str(Largest_Dec_Month + " $" + str(low)))
   
