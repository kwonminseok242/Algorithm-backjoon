n = int(input())
k = 0
answer = 0
for i in range(1, n+1):
    k = 1 + 2**i
    answer = k**2
    
print(answer)