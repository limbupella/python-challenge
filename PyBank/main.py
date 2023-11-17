import os
import csv

#set path
csvpath = os.path.join("Resources", "budget_data.csv")

#set list
total_months = []
total_profit = []
total_change_profits = [] 

#opening csv path
with open(csvpath, newline="") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    csv_header = next(budget_data)
    for row in budget_data:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
        total_change_profits.append(int(total_profit[i+1])-int(total_profit[i]))

increase = max(total_change_profits)
decrease = min(total_change_profits)

month_increase = total_change_profits.index(max(total_change_profits))+1
month_decrease = total_change_profits.index(min(total_change_profits))+1

print("Fianacial Analysis")
print("--------------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(total_change_profits)/len(total_change_profits),2)}")
print(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")

output = os.path.join(".","financial_analysis.txt")
with open(output,"w") as new:
    new.write('Financial Analysis')
    new.write("\n")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(total_months)}")
    new.write(f"Total: ${sum(total_profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(total_change_profits)/len(total_change_profits),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(increase))})")
    new.write(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(decrease))})")

