# 8958번 OX퀴즈
n = int(input())
ex = []
for i in range(n):
    k = str(input())
    sum = 0
    count = 0
    for i in k:
        if i == 'O':
            count += 1
            sum += count
        else:
            count = 0
    print(sum)

