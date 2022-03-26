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

# 다른 풀이

# n = int(input())

# nums_pileup = 1  # 벌집의 개수, 1개부터 시작
# cnt = 1

# while n > nums_pileup :
#     nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
#     cnt += 1
# print(cnt)