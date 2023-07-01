month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0

a, b = map(int, input().split())

for i in range(a - 1): # 요일을 구하는 방법은 day를 다 더해서 7로 나누면 요일이 나옴
    day += month[i]

day = (day + b) % 7 # 더해서 누적된 day를 7로 나누기
print(week[day])