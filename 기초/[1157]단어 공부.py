import sys
import string

S = sys.stdin.readline().lower()

alpha_ls = string.ascii_lowercase

alpha_ct = []

for i in alpha_ls:
    count = 0
    for j in S:
        if i == j:
            count += 1
    alpha_ct.append(count)

max_ls = [i for i in alpha_ct if i == max(alpha_ct)]

if len(max_ls) == 1:
    print(alpha_ls[alpha_ct.index(max(alpha_ct))].upper())
else :
    print('?')