import os
import csv

#file paths
budget_data = os.path.join('Resources', 'budget_data.csv')

#create import lists for the CSV data
month_list = []
profit_loss_list = []

# import the csv file
with open(budget_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader=next(csvfile)
    

    for row in csvreader:
        month_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))

# total months
total_months = len(month_list)

# total profit
total_profit_loss = 0

for x in profit_loss_list:
    total_profit_loss = total_profit_loss + x

# the average profit/loss
average_monthly_change_list = []
previous_month_amount = 0

for x in range(len(profit_loss_list)):
    if x == 0:
        previous_month_amount = profit_loss_list[x]
    else:
        monthly_change = profit_loss_list[x] - previous_month_amount
        average_monthly_change_list.append(monthly_change)
        previous_month_amount = profit_loss_list[x]

#print(average_monthly_change_list)

length = len(average_monthly_change_list)
total = sum(average_monthly_change_list)
profit_loss_average = total / length
print(profit_loss_average)

# the minimum and maximum profit vs. loss per month
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

# The total number of months included in the dataset
print(f'Total Months: {total_months}')

# The net total amount of "Profit/Losses" over the entire period
print(f'Total: ${total_profit_loss}')

# The average of the changes in "Profit/Losses" over the entire period
print(f'Average Change: ${round(profit_loss_average,2)}')

# The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {month_greatest_increase} (${amount_greatest_increase})')

# The greatest decrease in losses (date and amount) over the entire period
print(f' Greatest Decrease in Profits: {month_greatest_decrease} (${amount_greatest_decrease})')

#output data to csv file

output_path = os.path.join("Analysis", "Financial_Analysis_IL.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerows([
            ["Total Months: " + str(total_months)],
            ["Total Revenue: $" + str(total_profit_loss)],
            ["Average Revenue Change: $" + str(round(profit_loss_average,2))],
            ["Greatest Increase in Profit:" + str(month_greatest_increase) + "($ " + str(amount_greatest_increase) + ")"],
            ["Greatest Increase in Profit:" + str(month_greatest_decrease) + "($ " + str(amount_greatest_decrease) + ")"] ])