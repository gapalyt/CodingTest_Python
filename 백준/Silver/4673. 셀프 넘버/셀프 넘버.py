all_number = list(range(1, 10001))
remove_number = []

for num in all_number:
    new_num = num # num으로 초기화
    for number in str(num): # d(n)을 구하기 위해 변환
        new_num += int(number) # d(n)의 값 확보
    remove_number.append(new_num)

result = sorted(set(all_number) - set(remove_number)) # 셀프 넘버만 남음

for final in result:
    print(final)