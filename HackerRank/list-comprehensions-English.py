# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

input = stdin.readlines()
[X, Y, Z, N] = map(int, input)

print [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if (x+y+z) != N]
