import sys
from collections import deque

# n명과 순서k번 입력
N, K = map(int, sys.stdin.readline().split())

# 입력받은 n명 queue에 넣기
queue = deque([num for num in range(1, N + 1)])

# 제거된 사람들의 번호 result에 넣기
result = []

# 순서대로 k번째 사람 제거
while queue: # 큐가 빈 상태가 될 때까지 반복
    for _ in range(K - 1):  # K번째 사람을 맨 앞으로 이동
        queue.append(queue.popleft()) # popleft는 첫 번째 원소 제거
    result.append(str(queue.popleft()))  # K번째 사람을 큐에서 제거하고, 그 사람의 번호를 리스트에 넣기

# 출력 형식에 맞게 정답 출력
people = ", ".join(result)
print("<" + people + ">")