import sys
from collections import deque

def bfs(start, end): # 시작 위치와 목표 위치
    queue = deque()
    queue.append((start, 0)) # 현재 위치와 목표 위치에 도달하는데 걸린 시간을 큐에 추가
    visited = [False] * 100001 # 방문 여부 저장하는 리스트
    visited[start] = True  # 시작 위치는 방문한 것으로 표시

    while queue: # 큐가 비어있지 않는다면 계속 반복
        curr_location, time = queue.popleft() # 큐의 가장 앞에 있는 것을 꺼내서 현재 위치와 위치에 도달하는데 걸린 시간의 변수에 넣기

        if curr_location == end: # 현재 위치와 목표 위치가 동일하다면
            print(time) # 최소 시간인 time 출력

            break # 조건을 만족하면 탐색 종료

        # 수빈이가 이동할 수 있는 방법 3가지를 리스트에 저장
        next_positions = [curr_location - 1, curr_location + 1, curr_location * 2]

        for next_pos in next_positions:
            if (0 <= next_pos <= 100000) and not visited[next_pos]: # 문제에서 주어진 수빈이이가 있는 위치인 N의 조건과 방문 여부 저장한 리스트에 False라면
                queue.append((next_pos, time + 1)) # 조건을 만족하는 위치인 next_pos와 위치에 도달하는데 걸린 시간을 큐에 추가. time + 1인 이유는 이동하는데 걸리는 시간이 현재 위치로부터 1초 더 걸려서
                visited[next_pos] = True # 방문한 것으로 표시

# 입력 받기
N, K = map(int, sys.stdin.readline().split())
bfs(N, K)