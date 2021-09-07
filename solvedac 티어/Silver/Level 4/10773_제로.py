import sys

stake = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:    stake.pop(-1)
    else:    stake.append(n)
print(sum(stake))