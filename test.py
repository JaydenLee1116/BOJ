import sys
<<<<<<< HEAD

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

num_max = max(arr)

arr_new = []
a = 0
for i in arr:
    a += (i / num_max * 100)

print(a / N)
=======
>>>>>>> a956b74de92c3c94304e5cfbc372822a88d56df0
