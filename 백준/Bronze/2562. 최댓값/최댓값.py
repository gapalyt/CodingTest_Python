import sys

num_list = []
for _ in range(9):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list_max = max(num_list)
num_list_max_index = num_list.index(num_list_max)

print(num_list_max)
print(num_list_max_index + 1)