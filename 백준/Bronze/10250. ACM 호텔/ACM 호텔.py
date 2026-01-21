test_num = int(input())

for i in range(test_num):
    floor, room, visit = map(int, input().split())
    if visit%floor > 0:
        floor_num = visit%floor # 층수 구하기
    else:
        floor_num = floor
    room_num = 0
    count = 1
    floor_1 = floor

    while True:                 # 호수구하기 반복문
        if floor_1 >= visit:
            room_num = count
            break
        floor_1 = floor
        count += 1
        floor_1 *= count
    if room_num < 10:
        print(f'{floor_num}0{room_num}')
    else:
        print(f'{floor_num}{room_num}')