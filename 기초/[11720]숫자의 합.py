import sys

N = int(sys.stdin.readline())

n = sys.stdin.readline()

tot = 0

for i in range(N):
    tot += int(n[i])

print(tot)