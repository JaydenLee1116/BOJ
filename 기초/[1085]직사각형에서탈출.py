import sys

x, y, w, h = map(int, sys.stdin.readline().split())

if x < w / 2:
    if y < h / 2:
        print(min(x,y))
    else:
        print(min(x,h-y))
else:
    if y < h / 2:
        print(min(w-x,y))
    else:
        print(min(w-x,h-y))