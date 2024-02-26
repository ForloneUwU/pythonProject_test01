import csv
#открыть
with open('students.csv', encording='utf8') as file:
    reader = list(csv.reader(file,delimiter=','))[1:]

with open('students1.csv','w',encording='utf8',newline='') as file:
    writer = csv.writer(file,delimiter=',')