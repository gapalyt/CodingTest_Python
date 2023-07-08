import sys

N, M = map(int, sys.stdin.readline().split(" "))
basket = [0] * N

for m in range(M):
    i, j, k = map(int, sys.stdin.readline().split(" "))
    
    for k_num in range(i, j + 1):
        basket[k_num - 1] = k
        
for n in range(N):
    print(basket[n], end = " ")