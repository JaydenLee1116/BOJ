import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

if B >= C:
    print(-1)
else:
    nums = A // (C - B)
    print(nums + 1)