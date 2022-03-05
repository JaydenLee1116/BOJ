import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B, end='\n')