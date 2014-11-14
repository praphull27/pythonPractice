from sys import stdin
input = stdin.readlines()
text = input[0].strip()
pattern = input[1].strip()

# allow indexing into pattern and protect against change during yield
pattern = list(pattern)

# build table of shift amounts
shifts = [1] * (len(pattern) + 1)
shift = 1
for pos in range(len(pattern)):
    while shift <= pos and pattern[pos] != pattern[pos-shift]:
        shift += shifts[pos-shift]
    shifts[pos+1] = shift

# do the actual search
startPos = 0
matchLen = 0
count = 0
for c in text:
    while matchLen == len(pattern) or \
          matchLen >= 0 and pattern[matchLen] != c:
        startPos += shifts[matchLen]
        matchLen -= shifts[matchLen]
    matchLen += 1
    if matchLen == len(pattern):
        count += 1
print count
