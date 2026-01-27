# 9506번 약수들의 합
n = 0
while n != -1:
    n = int(input())
    if n == -1:
        break
    # 약수리스트
    s = []
    # 약수 구하기
    for i in range(1,n):
        if n % i == 0:
            s.append(i)

    if sum(s) == n:
        text = f'{n} = '
        for i in range(len(s)):
            if s[i] == s[len(s)-1]:
                text = text + f'{str(s[i])}'
                
            else:
                text = text + f'{str(s[i])} + '
            
        print(text)
    else:
        print(f'{n} is NOT perfect.')    



