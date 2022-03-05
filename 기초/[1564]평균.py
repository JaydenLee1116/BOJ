import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

num_max = max(arr)

a = 0

for i in arr:
    a += (i / num_max * 100)

print(a / N)