import sys
import random

find = []

for _ in range(9):
    find.append(int(sys.stdin.readline()))

# 첫 풀이
# while True:
#     temp = random.sample(find, 7)
#     if sum(temp) == 100:
#         break

# temp.sort()

# for i in temp:
#     print(i, sep='\n')

for i in range(9):
    for j in range(i+1,9):
        if sum(find) - find[i] - find[j] == 100:
            p = find[i]
            q = find[j]
            break

find.remove(p)
find.remove(q)

find.sort()

for i in find:
    print(i, sep='\n')