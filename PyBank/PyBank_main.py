import os
import csv

#list for data
date=[]
profit_losses=[]

#file paths
budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

  #row is python list from csv file 
  #counting months
    monthrow=0
    for row in csvreader:
        date.append(row[0])
        profit_losses.append(row[1])
        monthrow += 1

        #print(monthrow)
#greatest increase and decrease calculations

Greatest_Increase = profit [0]
Greatest_Decrease = profit [0]

total_profit=0

for p in profit:
    total_profit +=int(p)

for i in range (len(profit)):
    if revenue [i] >=Greatest_Increase:
        Greatest_Increase=profit[i]
        Greatest_Inc_Month=date[i]

        elif profit[i] <= Greatest_Decrease:
            Greatest_Decrease = profit [i]
            Greatest_Dec_Month= date[i]

average_change=roung(total_profit/monthrow, 2)


        

