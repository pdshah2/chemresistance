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
