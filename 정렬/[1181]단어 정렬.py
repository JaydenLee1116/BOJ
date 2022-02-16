import sys

N = int(sys.stdin.readline())

strings = []

for _ in range(N):
    strings.append(sys.stdin.readline().rstrip())

strings = set(strings)
strings = list(strings)

strings.sort()
strings.sort(key=lambda x : len(x))

for i in range(len(strings)):
    print(strings[i], sep="\n")