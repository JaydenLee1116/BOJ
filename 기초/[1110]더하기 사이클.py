import sys

N = int(sys.stdin.readline())
S = N

count = 0

while True:
    N = (N % 10) * 10 + (N // 10 + N % 10) % 10
    count += 1
    if N == S:
        print(count)
        break
    else:
        continue