import csv
import matplotlib.pyplot as mt

csvfile1 = open("file.csv","r")
rowList = csv.DictReader(csvfile1)

v_no = {}

for row in rowList:
    if row['Vehicle'] in v_no:
          v_no[row['Vehicle']]=v_no[row['Vehicle']]+1
    else:
          v_no[row['Vehicle']]=1
print(v_no)

data = []
for row in v_no:
     data.append(v_no[row])
print(mt)

labels = 'heavy', 'light'
colors = ['blue','yellow']
e=(0.1,0.1)

mt.pie(data,explode=e,labels=labels,colors=colors,startangle=90)
mt.axis('equal')
mt.show()
