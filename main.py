import csv

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

print(opencsv('./data/고용형태별_임금_및_근로시간.csv'))

