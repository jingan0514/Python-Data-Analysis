import os
import csv

csvpath = os.path.join('.', 'election_data.csv')
data = []
candidate = {}
num = 0
result = {}

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for row in csvreader:
        data.append(row[2])
        candidate.update({row[2]: 1})
        candidate_list = list(candidate.keys())

textpath = os.path.join('.', 'Election Resultss.txt')
with open(textpath, 'w') as text:

    print('Election Results')
    text.write('Election Results\n')
    print('----------------')
    text.write('----------------\n')
    total = len(data)
    print(f'Total Votes: {total}')
    text.write(f'Total Votes: {total}\n')
    print('----------------')
    text.write('----------------\n')
    for i in range(len(candidate_list)):
        for j in range(len(data)):
            if data[j] == candidate_list[i]:
                num += 1
        
        percent = round(num / total * 100.0, 3)
        print(f'{candidate_list[i]}: {percent}% ({num})')
        text.write(f'{candidate_list[i]}: {percent}% ({num})\n')
        result.update({num: candidate_list[i]})

        num = 0

    print('----------------')
    text.write('----------------\n')
    winner = result[max(result.keys())]
    print(f'Winner: {winner}')
    text.write(f'Winner: {winner}\n')
    print('----------------')
    text.write('----------------\n')