import sys

W_fin, H_fin = map(int, sys.stdin.readline().rstrip().split())


N_tot = int(sys.stdin.readline())

W = [0]
H = [0]


for _ in range(N_tot):
    direction, num = map(int, sys.stdin.readline().rstrip().split())
    if direction == 0:
        H.append(num)
    else:
        W.append(num)

H.append(H_fin)
W.append(W_fin)
H.sort()
W.sort()

dif_H=[]
dif_W=[]

for i in range(len(H)-1):
    dif_H.append(H[i+1] - H[i])
for i in range(len(W)-1):
    dif_W.append(W[i+1] - W[i])

print(max(dif_H) * max(dif_W))