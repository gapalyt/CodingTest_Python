import sys

N = int(sys.stdin.readline()) # 내가 가고 싶은 채널
M = int(sys.stdin.readline()) # 고장난 버튼의 갯수

removed_button = [1 for _ in range(10)] # 고장난 버튼 초기화

if (M != 0):
    removed = list(map(int, sys.stdin.readline().split(' ')))

    for i in range(M):
        removed_button[removed[i]] = 0

def is_possible(channel):
    channel = str(channel)

    for c in channel:
        if (removed_button[int(c)] == 0):
            return False

    return True # '7' -> 7, '8' -> 8, '6' -> 6. 그래서 c를 int(c)로 함.

answer = abs(N - 100)

for channel in range(0, 1000000):
    if is_possible(channel):
        num = len(str(channel)) # 786 -> '786' -> 3
        num += abs(N - channel) # abs는 절대값
        answer = min(answer, num)

print(answer)