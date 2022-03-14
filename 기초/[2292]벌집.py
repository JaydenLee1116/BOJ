import sys

N = int(sys.stdin.readline())
i = 0
if N ==1 :
    print(1)
else:
    while True:
        if ((N - 2) // 6) in range( i * ( i + 1 ) // 2, i * ( i + 3 ) // 2 + 1):
            print(i + 2)
            break
        else:
            i += 1