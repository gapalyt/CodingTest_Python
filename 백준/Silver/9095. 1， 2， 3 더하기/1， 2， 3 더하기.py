import sys

def sum_way(N):
    if N == 0: # 1, 2, 3의 합으로 나타내는 방법의 수
        return 1 # way[0] = 0

    way = [0] * (N + 1) # 1, 2, 3의 합으로 나타내는 방법의 수 저장
    way[0] = 1 # 초기값

    for i in range(1, N + 1):
        way[i] = way[i - 1]

        if i - 2 >= 0:
            way[i] += way[i - 2]

        if i - 3 >= 0:
            way[i] += way[i - 3]

    return way[N] # 1, 2, 3의 합으로 나타내는 방법의 수 구함

def main():
    T = int(sys.stdin.readline())  # 테스트 케이스 개수

    for _ in range(T):
        N = int(sys.stdin.readline())  # 1, 2, 3의 합으로 나타내는 수

        print(sum_way(N))

main()