import sys

alp_arr = sys.stdin.readline().rstrip()

time_tot = 0

for alp in alp_arr:
    if alp in 'ABC':
        time_tot += 3
    elif alp in 'DEF':
        time_tot += 4
    elif alp in 'GHI':
        time_tot += 5
    elif alp in 'JKL':
        time_tot += 6
    elif alp in 'MNO':
        time_tot += 7
    elif alp in 'PQRS':
        time_tot += 8
    elif alp in 'TUV':
        time_tot += 9
    else:
        time_tot += 10

print(time_tot)