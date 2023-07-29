# n번 입력
n = int(input())

# 리스트 안에 0과 1을 넣어줌
result = [0, 1]

# n이 2부터 입력한 n번까지 구해서 리스트에 넣기
for num in range(2, n + 1):
    result.append(result[num - 2] + result[num - 1])

# 리스트의 n번째 출력
print(result[n])