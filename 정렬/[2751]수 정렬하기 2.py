import sys

N = int(sys.stdin.readline())

def fact(N):
    if N <= 1:
        return 1
    else:
        return N * fact(N-1)

print(fact(N))