import sys
import math

A, B, V = map(int, sys.stdin.readline().rstrip().split())

D = math.ceil((V - A) / (A - B)) + 1

print(D)