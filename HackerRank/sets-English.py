# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

input = stdin.readlines()
m = int((input[0]).strip())
M = set(map(int, ((input[1]).strip()).split()))
n = int((input[2]).strip())
N = set(map(int, ((input[3]).strip()).split()))
outputList = sorted(list((M.difference(N)).union(N.difference(M))))
for item in outputList:
    print item
