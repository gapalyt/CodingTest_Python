import math

def solution(num1, num2):
    answer1 = num1 / num2 * 1000
    answer2 = math.trunc(answer1)
    
    return answer2