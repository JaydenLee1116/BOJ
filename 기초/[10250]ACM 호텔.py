import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    
    if N % H ==0:
        ans = H * 100 + N // H
    else:
        ans = (N % H) * 100 + N // H + 1
    print(ans)