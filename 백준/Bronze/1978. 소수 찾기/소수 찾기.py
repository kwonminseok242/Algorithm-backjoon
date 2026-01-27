# 1978번 소수 찾기
n = int(input())
num = list(map(int, input().split()))
sosu = 0
for i in range(n):
    count = 0
    
    for j in range(1,num[i]+1):
        if num[i] % j == 0:
            count += 1
    if count == 2:
        sosu += 1
        
print(sosu)