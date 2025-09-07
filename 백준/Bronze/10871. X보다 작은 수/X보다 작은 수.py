n,m = map(int, input().split())
num = list(map(int, input().split()))
for i in num:
    if i < m:
        print(i, end=" ")
