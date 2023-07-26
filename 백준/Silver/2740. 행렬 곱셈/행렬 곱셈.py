import sys

# 행렬 A 입력 받기
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 행렬 B 입력 받기
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 결과 행렬 초기화
result = []

for _ in range(N):
    row = [0] * K
    result.append(row)

# 행렬 곱하기
for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += A[n][m] * B[m][k]

# 곱한 행렬의 각 행 출력
for f in result:
    print(*f)
