import numpy as np
import csv

with open('Sangir-Chemical-resistance-Chart.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

def hasdigit(l):
    for item in l:
        if str.isdigit(item): return True
    return False

data = [d for d in data if hasdigit(d)]

header = 'Medium Concentration(%) PVC CPVC ABS PE PP PVDF FRP FRB FRV FRVS FRE FRHA FRF FRPH'.split()

for i in range(len(data)):

    if data[i][0] == '': data[i][0] = data[i-1][0]

data_dict = dict()
for d in data:
    if d[0] not in data_dict: data_dict[d[0]] = d[1:]

    else: data_dict[d[0]] = data_dict[d[0]] + [d[1:]]


len(data_dict)

for d in data: print(d[0])


len(data_dict['Waste gases contianing'])


a = [1, 2, 3]
b = [4, 5, 6]
a + b

[a] + [a]
