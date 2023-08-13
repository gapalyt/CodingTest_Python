import sys

def TSP(graph, N, visited, current, start):
    if visited == (1 << N) - 1:  # 모든 도시를 방문한 경우 검사

        # 만약 현재 도시에서 시작 도시로 가는 비용이 양수인 경우 해당 비용을 반환하고, 아니면 매우 큰 값을 반환
        return graph[current][start] if graph[current][start] > 0 else sys.maxsize

    min_cost = sys.maxsize # 초기화

    for i in range(N):
        if not (visited & (1 << i)) and graph[current][i] > 0: # 현재 도시에서 i번 도시로 가는 경로가 가능 & 아직 방문하지 않은 경우
            cost = graph[current][i] + TSP(graph, N, visited | (1 << i), i, start) # 비용 계산
            min_cost = min(min_cost, cost) # 최소 비용

    return min_cost

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)] # 각 도시간의 비용

start = 0 # 시작 도시
answer = TSP(graph, N, 1 << start, start, start) # TSP 함수 호출해서 최소 비용 계산

print(answer) # 최소 비용 출력