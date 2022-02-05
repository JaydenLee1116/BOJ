import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a = sys.stdin.readline().split('X')
    total = 0
    for value in a:
        total += sum(range(value.count('O') + 1))
    print(total)