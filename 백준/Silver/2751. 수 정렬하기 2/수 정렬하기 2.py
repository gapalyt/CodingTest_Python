import sys

N = int(sys.stdin.readline().strip())
N_list = []

for i in range(N):
    num = int(sys.stdin.readline().strip())
    N_list.append(num)
    
N_list.sort()

for k in range(N):
    print(N_list[k])