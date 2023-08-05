import sys

def dfs(depth, idx): # 선택된 숫자의 개수, 선택할 숫자의 인덱스
        if depth == 6:
            for num in lotto_list:
                print(num, end = ' ') # 지금까지 선택된 로또 번호 조합 출력

            print() # 줄바꿈

            return

        for jdx in range(idx, k): # k는
            lotto_list.append(s[jdx])
            dfs(depth + 1, jdx + 1) # 재귀 호출을 하기 위해
            lotto_list.pop() # 만약 조건이 맞지 않으면 이전 선택 단계로 돌아가기 위해 마지막으로 추가한 숫자 제거

while True:
    lotto = list(map(int, sys.stdin.readline().split()))

    if lotto[0] == 0:
        break

    k = lotto[0] # 입력된 숫자의 개수 저장
    s = lotto[1:] # 실제로 선택할 수 있는 숫자 저장
    lotto_list = [] # 로또 번호 조합

    dfs(0, 0) # dfs 호출

    print() # 하나의 입력이 처리되면 빈 줄 출력