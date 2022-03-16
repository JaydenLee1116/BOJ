import sys

X = int(sys.stdin.readline())

line = 0  # 대각선 라인
max_num = 0  # 라인에서 가장 큰 수
while X > max_num:
    line += 1  
    max_num += line  

gap = max_num - X 

# 홀수일 때
top = gap + 1  
under = line - gap  

# 짝수일 때
if line % 2 == 0: 
    top = line - gap  
    under = gap + 1  

print(f'{top}/{under}')