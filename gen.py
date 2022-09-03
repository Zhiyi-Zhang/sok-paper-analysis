import csv
import json
from string import Template
class MyTemplate(Template):
    delimiter = '|'
    idpattern = r'[a-z]+'

selected_cols = [0,1,2,3,6,19]
result = []
with open('ddos-paper-merged - Aug29,2022.csv','r', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        result.append([row[x] for x in selected_cols])


f = open('template.html','r')
template = MyTemplate( f.read())
f.close()

out = open('index.html', 'w')
out.write(template.substitute(paperData=json.dumps(result[1:])))
out.close()
#print(result[1:])
