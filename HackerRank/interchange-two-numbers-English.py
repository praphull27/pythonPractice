# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdin
input = stdin.readlines()
[X, Y] = map(int, input)
t = (X, Y)
X = t[1]
Y = t[0]
print X
print Y
