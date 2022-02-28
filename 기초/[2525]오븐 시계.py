import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

C = int(sys.stdin.readline())

if B + C >= 60:
    D = (B + C) // 60
    E = (B + C) % 60

    if A + D >= 24:
        F = A + D - 24
        print(F, E)
    else:
        print(A + D, E)
else:
    print(A, B + C)