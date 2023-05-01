import csv
import pandas as pd
def data(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

print(data('./data/직종별_임금_및_근로시간.csv'))




