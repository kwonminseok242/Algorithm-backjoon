# 11653번 소인수분해
n = int(input())
k = 2
s = []
for i in range(n):
    if n%k == 0:
        n = n/k
        s.append(k)
        continue
    else:
        k +=1
for i in s:
    print(i)
