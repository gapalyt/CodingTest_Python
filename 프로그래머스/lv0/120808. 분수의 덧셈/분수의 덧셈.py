import math

def solution(numer1, denom1, numer2, denom2):
    answer1 = denom1 * denom2
    answer2 = numer1 * denom2 + numer2 * denom1
    answer3 = math.gcd(answer1, answer2)
    
    return [answer2 // answer3, answer1 // answer3]