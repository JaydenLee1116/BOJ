import sys

alp_cro = sys.stdin.readline().rstrip()

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alp in arr:
    if alp in alp_cro:
        alp_cro = alp_cro.replace(alp, '*')

print(len(alp_cro))