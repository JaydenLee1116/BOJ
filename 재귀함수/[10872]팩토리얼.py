import sys

N = int(sys.stdin.readline())

N_list = list(range(1, N+1))

answer = 1
for num in N_list:
    answer *= num

print(answer)