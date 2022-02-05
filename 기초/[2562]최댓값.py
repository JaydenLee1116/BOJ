import sys

a = []

for i in range(9):
    a.append(int(sys.stdin.readline()))
    
print(max(a))

for i in range(9):
    if a[i] == max(a):
        print(i+1)