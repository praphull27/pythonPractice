# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
input = stdin.readlines()
N = int(input.pop(0))
students = []
for i in range(N):
    line = ((input.pop(0)).strip()).split()
    record = {}
    record['name'] = line[0]
    record['maths'] = float(line[1])
    record['physics'] = float(line[2])
    record['chemistry'] = float(line[3])
    students.append(record)
query = (input.pop(0)).strip()
for i in range(N):
    if query == students[i]['name']:
        avg = (students[i]['maths'] + students[i]['physics'] + students[i]['chemistry']) / 3.0
        print"%.2f" % avg
