import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().rstrip().split()))

C = []

for i in B:
    if i in A:
        C.append(1)
    else:
        C.append(0)

for j in C:
    print(j, sep='\n')