import os
import csv

#list for data
date=[]
profit=[]

#file paths
budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

  #row is python list from csv file 
  #counting months
    month_row=0
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
        month_row += 1
print("Total Months:" + str(month_row))


#greatest increase and decrease calculations

greatest_increase = profit [0]
greatest_decrease = profit [0]

total_profit=0

for p in profit:
    total_profit +=int(p)

for i in range (len(profit)):
    if profit[i] >=greatest_increase:
        greatest_increase=profit[i]
        greatest_inc_month=date[i]

    elif profit[i] <= greatest_decrease:
        greatest_decrease = profit[i]
        greatest_dec_month= date[i]

#average change calculation
average_change=round(total_profit/month_row, 2)

#print data to python terminal
print("Financial Analysis")
print("Total Months:" + str(month_row))
print("Total Revenue:" + str(total_profit))
print("Average Revenue Change:" + str(average_change))
print("Greatest Increase in Profit:" + str(greatest_inc_month) + "($ " + str(greatest_increase) + ")")
print("Greatest Decrease in Profit:" + str(greatest_dec_month) + "($ " + str(greatest_decrease) + ")")

#output data to csv file

output_path = os.path.join("Analysis", "Financial_Analysis_IL.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerows([
            ["Total Revenue: $" + str(total_profit)],
            ["Total Months:" + str(month_row)],
            ["Average Revenue Change:" + str(average_change)],
            ["Greatest Increase in Profit:" + str(greatest_inc_month) + "($ " + str(greatest_increase) + ")"],
            ["Greatest Increase in Profit:" + str(greatest_dec_month) + "($ " + str(greatest_decrease) + ")"] ])




        

