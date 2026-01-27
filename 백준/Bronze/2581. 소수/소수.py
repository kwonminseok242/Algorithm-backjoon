m = int(input())
n = int(input())
s = []

for i in range(m, n + 1):
    if i == 1: # 1은 소수가 아니므로 건너뜀
        continue
    
    # 약수 발견 여부를 체크하는 변수 (Flag)
    is_prime = True 
    
    # 2부터 i-1까지 나누어 봅니다.
    for j in range(2, i): 
        if i % j == 0:
            is_prime = False # 약수가 발견되었으므로 소수가 아님
            break # 더 이상 검사할 필요 없이 탈출! (시간 절약의 핵심)
    
    if is_prime:
        s.append(i)

if s == []:
    print(-1)
else:
    print(sum(s))
    print(min(s))