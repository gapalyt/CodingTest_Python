import sys
from collections import deque

# 큐에 X 넣기
def push(queue, X):
    queue.append(X)

# 큐에서 가장 앞에 있는 정수 빼기
def pop(queue):
    if not queue: # 큐에 정수가 없는 경우
        return -1 # -1 반환
    return queue.popleft() # 큐에 정수가 있으면 첫 번째 원소 빼기

# 큐에 들어있는 정수의 개수 출력
def size(queue):
    return len(queue) # 큐의 길이 반환

# 큐가 비어있으면
def empty(queue):
    if not queue: # 큐에 정수가 없는 경우
        return 1 # 1을 반환
    return 0 # 정수가 있다면 0을 반환

# 큐의 가장 앞에 있는 정수 출력
def front(queue):
    if not queue: # 큐에 정수가 없는 경우
        return -1 # -1 반환
    return queue[0] # 정수가 있다면 가장 앞에 있는 정수 반환

# 큐의 가장 뒤에 있는 정수 출력
def back(queue):
    if not queue: # 큐에 정수가 없는 경우
        return -1 # -1 반환
    return queue[-1] # 정수가 있다면 가장 뒤에 있는 정수 반환

#
def main():
    N = int(sys.stdin.readline()) # 첫째 줄에 주어지는 명령의 수 입력
    queue = deque() # 큐 생성

    for _ in range(N):
        command = sys.stdin.readline().split()

        if (command[0] == 'push'):
            push(queue, int(command[1]))

        elif (command[0] == 'pop'):
            print(pop(queue))

        elif (command[0] == 'size'):
            print(size(queue))

        elif (command[0] == 'empty'):
            print(empty(queue))

        elif (command[0] == 'front'):
            print(front(queue))

        elif (command[0] == 'back'):
            print(back(queue))
main()