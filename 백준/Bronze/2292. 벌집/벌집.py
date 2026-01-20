num = int(input())
b = 1  # 현재 층
k = 1  # 현재 층의 마지막 방 번호

if num == 1:
    print(1)
else:
    while k < num:
        k += 6 * b
        b += 1
    
    print(b)