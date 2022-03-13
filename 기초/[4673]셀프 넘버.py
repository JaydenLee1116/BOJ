rm_list = []

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    if i < 10000:
        rm_list.append(i)

tot_list = list(range(1, 10000))

for k in set(rm_list):
    tot_list.remove(k)

for n in tot_list:
    print(n)