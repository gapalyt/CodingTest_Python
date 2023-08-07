import sys

def dfs(day, profit): # 현재 날짜와 누적된 이익
    global max_profit # 더 큰 값을 저장하기 위해 전역 변수 사용

    if day == N + 1: # 현재 날짜가 퇴사일 다음날인 경우
        max_profit = max(max_profit, profit) # 둘 중 더 큰 값을 저장

        return # 종료

    if day > N + 1: # 현재 날짜가 퇴사일을 넘어간 경우
        return # 종료

    # 상담을 하는 경우
    dfs(day + T[day], profit + P[day]) # 누적된 이익에 현재 상담으로 얻는 이익을 더함

    # 상담을 건너뛰는 경우
    dfs(day + 1, profit)

N = int(sys.stdin.readline()) # 전체 일정
T = [0] * (N + 1) # 일정 날짜
P = [0] * (N + 1) # 일정 날짜

for i in range(1, N + 1):
    T[i], P[i] = map(int, sys.stdin.readline().split()) # 날짜 별 상담시간과 상담으로 얻는 이익

max_profit = 0 # 초기화
dfs(1, 0) # 첫 날짜인 1일부터 시작하는데 누적된 이익은 0

print(max_profit) # 최대 이익 출력