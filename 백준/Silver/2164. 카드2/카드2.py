import sys
from collections import deque

def last_card(N):
    card = deque(range(1, N + 1)) # 1부터 N까지의 숫자를 큐에 넣기

    while len(card) > 1: # 카드의 길이가 1보다 크면 계속 반복
        card.popleft() # 첫 번째 카드 제거
        card.append(card.popleft()) # 새로운 맨 앞에 있는 카드를 덱의 맨 뒤에 추가

    return card[0] # 마지막으로 남은 카드 반환

N = int(sys.stdin.readline())

print(last_card(N))