import math

n = int(input())
a = list(map(int, input().split()))
b,c = map(int, input().split())

count = 0

for i in range(n):
    num = a[i]-b
    if num < 0:
        count = count + 1
    elif num == 0:
        count = count + 1
    else:
        h = num/c
        count = count + math.ceil(h)+1

print(count)