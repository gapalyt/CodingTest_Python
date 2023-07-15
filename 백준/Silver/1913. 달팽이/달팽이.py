n = int(input()) # 7
number = int(input()) # 35 특정값
direction =[[1,0],[0,1],[-1,0],[0,-1]] # down, right, up, left
snail = [[0 for _ in range(n)] for _ in range(n)]
start = n * n # 달팽이가 N^2 시작하는 값이고, 내림차순으로 들어간다
curr_y = 0
curr_x = 0
curr_dir = 0 # 0, 1, 2, 3 까지 들어가야함
solution = list() # 문제에서 원하는 특정값의 좌표값을 담기 위함
for _ in range(n * n):
    if start == number:
        solution = [curr_y + 1, curr_x + 1]
    snail[curr_y][curr_x] = start # 25
    next_y = curr_y + direction[curr_dir][0] # 1
    next_x = curr_x + direction[curr_dir][1] # 0
    #next_y = 5, next_x = 0
    if next_y < 0 or next_x < 0 or next_y >= n or next_x >= n or \
        snail[next_y][next_x] != 0:
        curr_dir += 1
        curr_dir = curr_dir % 4 # 0, 1, 2, 3
    # 바뀐 방향대로 다시 값을 업데이트 -> curr_dir이 바뀌었을 수 있음
    curr_y = curr_y + direction[curr_dir][0]
    curr_x = curr_x + direction[curr_dir][1]
    start -= 1
# 답을 출력하기 위한 for문: 달팽이와 특정값의 좌표값
for y in range(n):
    for x in range(n):
        print(snail[y][x], end=' ')
    print()
print(solution[0], solution[1]) # 좌표값 출력