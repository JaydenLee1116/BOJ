import sys
from statistics import mode

A, B, C = map(int, sys.stdin.readline().rstrip().split())

if A == B == C:
    print(10000 + 1000 * A)
elif (A == B != C) or (B == C != A) or (C == A != B):
    print(1000 + 100 * mode([A, B, C]))
else:
    print(100 * max([A, B, C]))