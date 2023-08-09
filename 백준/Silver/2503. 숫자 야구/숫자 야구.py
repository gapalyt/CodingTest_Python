import sys

def all_guess(guess, question, strike, ball): # 추측, 질문, 스트라이크, 볼
    guess_str = str(guess)
    question_str = str(question)
    guess_strike = guess_ball = 0 # 스트라이크와 볼읙 개수 초기화

    for i in range(3):
        if guess_str[i] == question_str[i]: # 현재 자릿수의 추측과 질문이 스트라이크인지 확인
            guess_strike += 1 # 스트라이크라면 증가
        elif guess_str[i] in question_str: # 현재 자릿수의 추측과 질문이 볼인지 확인
            guess_ball += 1 # 볼이면 증가

    return guess_strike == strike and guess_ball == ball # 계산된 스트라이크와 볼의 개수가 일치하는지 확인하고 결과를 반환

def backtrack(possible_numbers, guesses, index): # 자릿수의 숫자 결정
    if index == 3: # 현재 3자리인 경우
        return 1 # 경우의 수를 세는데 1 반환

    cnt = 0 # 경우의 수 초기화

    for num in possible_numbers:
        if all(all_guess(num, guess[0], guess[1], guess[2]) for guess in guesses): # 선택한 숫자가 주어진 모든 추측 조건을 만족하는지 확인
            next_possible_numbers = [n for n in possible_numbers if all_guess(n, num, 3, 0)] # 다음 자릿수에서 가능한 숫자 리스트 생성, 선택한 숫자와 스트라이크 3, 볼은 0
            cnt += backtrack(next_possible_numbers, guesses, index + 1) # 다음 자릿수를 탐색해서 경우의 수를 세고 결과를 경우의 수에 추가

    return cnt # 경우의 수 반환

def main():
    N = int(sys.stdin.readline())  # 질문 수 입력
    guesses = [] # 추측 조건을 저장할 리스트

    for _ in range(N):
        question, strike, ball = map(int, sys.stdin.readline().split())
        guesses.append((question, strike, ball))

    possible_numbers = [num for num in range(123, 988) if len(set(str(num))) == 3 and '0' not in str(num)] # 숫자의 각 자릿수가 모두 다르고 0이 포함되지 않도록 조건 설정하면서 가능한 숫자 리스트 생성
    answer = backtrack(possible_numbers, guesses, 0) # 백트래킹 함수 호출해서 가능한 경우의 수 세고, 결과 저장
    print(answer) # 가능한 경우의 수 출력

if __name__ == "__main__": # 스크립트가 직접 실행될 때만 실행
    main()