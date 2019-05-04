import os
import csv

filepath = os.path.join('.', 'budget_data.csv')

total_month = 0
total = 0
month = []
profit_and_loss = []
change = []

with open(filepath, newline = '') as budget_data:
    csvreader = csv.reader(budget_data, delimiter = ',')
    next(csvreader, None)
    for row in csvreader:
        month.append(row[0])
        profit_and_loss.append(int(row[1]))

total_month = len(month)
total = sum(profit_and_loss)

for i in range(1, len(profit_and_loss)):
    change.append(profit_and_loss[i] - profit_and_loss[i-1])

average = round(sum(change) / (len(month) - 1), 2)

increase = max(change)
month_in = month[change.index(increase) + 1]
decrease = min(change)
month_de = month[change.index(decrease) + 1]

print('Financial Analysis')
print('------------------')
print(f'Total Month: {total_month}')
print(f'Total: ${total}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {month_in} (${increase})')
print(f'Greatest Decrease in Profits: {month_de} (${decrease})')

textpath = os.path.join('.', 'Financial Analysis.txt')
with open(textpath, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('------------------\n')
    text.write(f'Total Month: {total_month}\n')
    text.write(f'Total: ${total}\n')
    text.write(f'Average Change: ${average}\n')
    text.write(f'Greatest Increase in Profits: {month_in} (${increase})\n')
    text.write(f'Greatest Decrease in Profits: {month_de} (${decrease})\n')