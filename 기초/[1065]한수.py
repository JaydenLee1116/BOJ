import sys

N = int(sys.stdin.readline().rstrip())

count = 0
for i in range(1, N+1):
    if len(str(i)) <= 2:
        count += 1
    else:
        i_str = str(i)
        if int(i_str[2]) - int(i_str[1]) == int(i_str[1]) - int(i_str[0]):
            count += 1
        else:
            continue

print(count)