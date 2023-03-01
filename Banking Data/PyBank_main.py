import os
import csv

#file paths
budget_data = os.path.join('Resources', 'budget_data.csv')

#create import lists for the CSV data
month_list = []
profit_list = []

# import the csv file
with open(budget_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader=next(csvfile)
    

    for row in csvreader:
        month_list.append(str(row[0]))
        profit_list.append(int(row[1]))

# total months
total_months = len(month_list)

# total profit
total_profit = 0

for x in profit_list:
    total_profit = total_profit + x

# the average profit/loss
average_monthly_change_list = []
previous_month_amount = 0

for x in range(len(profit_list)):
    if x == 0:
        previous_month_amount = profit_list[x]
    else:
        monthly_change = profit_list[x] - previous_month_amount
        average_monthly_change_list.append(monthly_change)
        previous_month_amount = profit_list[x]

#monthly change

length = len(average_monthly_change_list)
total = sum(average_monthly_change_list)
profit_loss_average = total / length
print(profit_loss_average)

# the minimum and maximum, increase/decrease per month
month_greatest_increase = ''
amount_greatest_increase = 0
month_greatest_decrease = ''
amount_greatest_decrease = 0

for x in range(len(average_monthly_change_list)):
    if average_monthly_change_list[x] > amount_greatest_increase:
        amount_greatest_increase = average_monthly_change_list[x]
        month_greatest_increase = month_list[x+1]
    elif average_monthly_change_list[x] < amount_greatest_decrease:
        amount_greatest_decrease = average_monthly_change_list[x]
        month_greatest_decrease = month_list[x+1]

# Total months
print(f'Total Months: {total_months}')

# Total of all profit
print(f'Total: ${total_profit}')

# Average Change calc
print(f'Average Change: ${round(profit_loss_average,2)}')

# Greatest increase calc
print(f'Greatest Increase in Profits: {month_greatest_increase} (${amount_greatest_increase})')

# Greatest decrease calc
print(f' Greatest Decrease in Profits: {month_greatest_decrease} (${amount_greatest_decrease})')

#output data to csv file

output_path = os.path.join("Analysis", "Financial_Analysis_IL.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerows([
            ["Total Months: " + str(total_months)],
            ["Total Revenue: $" + str(total_profit)],
            ["Average Revenue Change: $" + str(round(profit_loss_average,2))],
            ["Greatest Increase in Profit:" + str(month_greatest_increase) + "($ " + str(amount_greatest_increase) + ")"],
            ["Greatest Increase in Profit:" + str(month_greatest_decrease) + "($ " + str(amount_greatest_decrease) + ")"] ])