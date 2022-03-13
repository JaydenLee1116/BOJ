import sys

N = int(sys.stdin.readline())

n = sys.stdin.readline().rstrip()

tot = 0

# for i in range(N):
#     tot += int(n[i])

for i in n:
    tot += int(i)

print(tot)