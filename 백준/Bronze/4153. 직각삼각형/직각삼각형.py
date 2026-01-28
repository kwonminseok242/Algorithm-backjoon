# 4153 직각삼각형

while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break

    # 리스트에 abc를 넣어보자
    list = [a,b,c]
    max_num = max(list) # 가장 큰수
    list.remove(max_num)
    # 제곱
    squar = (list[0])**2 + (list[1])**2

    max_squar = max_num**2

    if squar == max_squar:
        print('right')
    else:
        print('wrong')