import sys

H, M = map(int, sys.stdin.readline().rstrip().split())

if H == 0 :
    if M >= 45:
        print(H, M-45)
    else:
        print(23, 60 + (M - 45))
else:
    if M >= 45:
        print(H, M-45)
    else:
        print(H-1, 60 + (M - 45))