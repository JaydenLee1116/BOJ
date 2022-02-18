import sys
from itertools import permutations

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for i in permutations(arr, N):
    sum=0
    for j in range(N-1):
        sum += abs(i[j] - i[j+1])
        if sum > ans :
            ans = sum

print(ans)