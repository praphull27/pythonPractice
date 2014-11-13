# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
input = stdin.readlines()
firstname = input[0].strip()
lastname = input[1].strip()

print "Hello %s %s! You just delved into python." % (firstname, lastname)
