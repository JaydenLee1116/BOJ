import sys

N = int(sys.stdin.readline())

for _ in range(N):
    R, S = sys.stdin.readline().rstrip().split()
    R = int(R)
    S = list(S)
    P = ''
    for i in range(len(S)):
        P += S[i] * R
    print(P)