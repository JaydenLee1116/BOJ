import sys

N = sys.stdin.readline().strip()

def solve(N):
    arr = []
    for i in range(int(N)+1):
        temp = i
        for j in list(str(temp)):
            temp += int(j)

        if temp == int(N):
            arr.append(i)
        else:
            pass
    if len(arr) == 0:
        return 0
    else:
        return min(arr)

print(solve(N))