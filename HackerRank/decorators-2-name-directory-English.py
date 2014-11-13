# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
from operator import itemgetter

input = stdin.readlines()
noOfLines = int((input.pop(0)).strip())
peopleList = []
for i in range(0,noOfLines):
    peopleList.append(((input[i]).strip()).split())

peopleList.sort(key=itemgetter(2))
for i in range(0,noOfLines):
    if (peopleList[i][3] == 'M'):
        print "Mr. " + peopleList[i][0] + " " + peopleList[i][1]
    else:
        print "Ms. " + peopleList[i][0] + " " + peopleList[i][1]