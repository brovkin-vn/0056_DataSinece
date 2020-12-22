import re
pattern = re.compile('\d+')
f = open('d:/aaa/0056_DataSinece/src/StudentsPerformance.csv') 
exams = []

for n, line in enumerate(f):
    if n > 0:
        info = line.split(',')
        new_line = []
        for item in info:
            if pattern.search(item) != None:
                new_line.append(int(pattern.search(item)[0]))
            else:
                new_line.append(item[1:-1])

        exams.append(new_line)        
cnt, v5, v6, v7, i = 0, 0, 0, 0, 0

for row in exams:       
    if row[3] == "free/reduced":
        cnt += 1
        v7 += row[7] 


v7 /= cnt 

print(v5, v6, v7, cnt, i)
f.close()