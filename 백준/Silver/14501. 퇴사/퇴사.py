import sys

def solution(N, schedules): # N은 최사까지 남은 날짜, schedules는 일정 리스트
    dp = [0] * (N + 1) # 초기값 0, 날짜별 최대 이익 저장하는 리스트

    for i in range(N - 1, -1, -1): # 역순으로 일정 확인
        day, profit = schedules[i] # 걸리는 기간과 이익
        next_day = i + day

        if next_day > N: # 다음 날이 퇴사일을 넘기는 경우
            dp[i] = dp[i + 1] # 현재 날짜의 최대 이익과 다음 날짜의 최대 이익 동일
        else:
            dp[i] = max(dp[i + 1], profit + dp[next_day]) # 둘 중 더 큰 값 선택

    return dp[0] # 첫 번째 날짜의 최대 이익 반환

if __name__ == "__main__": # 스크립트가 직접 실행될 때만 실행
    N = int(input())  # 퇴사까지 남은 날짜
    schedules = [] # 일정 리스트

    for _ in range(N): # 퇴사까지 남은 날짜 만큼 반복
        day, profit = map(int, sys.stdin.readline().split()) # 일정 소요와 이익 입력
        schedules.append((day, profit)) # 튜플로 만들어 리스트에 저장

    answer = solution(N, schedules) # 최대 이익 저장
    
    print(answer) # 최대 이익 출력