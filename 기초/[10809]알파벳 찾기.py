import sys
import string

S = sys.stdin.readline()

alpha_str = string.ascii_lowercase

for i in alpha_str:
    if i in S:
        print(S.index(i), sep=' ')
    else:
        print(-1, sep=' ')