# 설탕 배달(2839번): 가장 5kg을 많이 사용하면서 남은 것이 3으로 나누어 떨어져야 함.

N = int(input())
answer = -1

for five in range(N // 5 * 5, -1, -5): # 범위는 -1까지 설정했으나 -2까지 설정해도 상관없음
    left = N - five
    
    if (left % 3 == 0):
        answer = five // 5 + left // 3
        
        break
        
print(answer)