import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

arr = []

for i in range(M, N+1):
    temp = []
    for j in range(1, i+1):
        if i % j == 0:
            temp.append(j)
    if len(temp) == 2:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])