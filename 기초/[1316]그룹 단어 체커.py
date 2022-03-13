import sys

N = int(sys.stdin.readline())

for _ in range(N):
    noun = sys.stdin.readline().rstrip()
    arr = []
    temp = 0
    
    for alp in noun:
        arr.append(alp)
    
    if len(arr) == 1:
        continue
    else:
        for i in range(len(arr) - 1):
            if arr[i] != arr[i+1]:
                temp += 1
        if temp >= len(set(arr)):
            N -= 1
print(N)