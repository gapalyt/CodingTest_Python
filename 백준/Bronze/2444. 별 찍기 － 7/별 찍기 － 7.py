# 이렇게 사용 금지
N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * (2 * i - 1))
for i in range(N - 1, 0, -1):
    print(" " * (N - i) + "*" * (2 * i -1))

# 위와 같은 결과를 얻으려면 범위를 나누어야 하는데...
# 힌트는 for문 3개, 절대값 이용

