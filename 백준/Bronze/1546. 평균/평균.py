import sys

N = int(sys.stdin.readline())
grade = list(map(int, sys.stdin.readline().split()))
grade_max = max(grade)
average = []

for i in grade:
    average.append(i / grade_max * 100)

print(sum(average) / N)