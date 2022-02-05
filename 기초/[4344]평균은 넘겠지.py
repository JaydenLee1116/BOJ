import sys

C = int(sys.stdin.readline())

for _ in range(C):
    N = list(map(int, sys.stdin.readline().split()))
    count= 0 
    for i in range(N[0]):
        if N[i+1] > sum(N[1:]) / N[0]:
            count += 1
    print(format(count / N[0] * 100,'.3f'), end='%\n')