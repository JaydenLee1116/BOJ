import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

i = (A+B)%C
j = ((A%C) + (B%C))%C
k = (A*B)%C
l = ((A%C)*(B%C))%C

print(i)
print(j)
print(k)
print(l)