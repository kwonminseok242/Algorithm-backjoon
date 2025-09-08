n = int(input())  # 테스트 케이스 개수

for _ in range(n):
    a, b = input().split()
    a = int(a)
    P = ''
    for i in b:
        P += i * a
    print(P)