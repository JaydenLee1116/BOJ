import sys

A, B = sys.stdin.readline().rstrip().split()

A = list(A)
B = list(B)

A.reverse()
B.reverse()

A = int(''.join(A))
B = int(''.join(B))

print(max(A, B))