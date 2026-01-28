# 30802번 웰컴키트

# 티셔츠 사이즈는 6개 같은 사이즈끼리만 T장 묶음 구매가능 이건 부족하면 안된다.
# 펜은 한종류 P자루씩 묶음 주문 이건 남거나 부족해서는 안된다.

N = int(input()) # 참가자의 수
# 티셔츠 사이즈별 신청자 수 
S, M, L, XL, XXL, XXXL = map(int,input().split())
t_shirt = [S,M,L,XL,XXL,XXXL] # 리스트로 변환
count = 0
# 티셔츠와 펜의 묶음 수를 의미하는 T, P
# 그러니까 티셔츠 주문 개수랑 펜은 몫이랑 나머지 구하라는 거잖아.
T, P = map(int,input().split())

# T 구하는 반복문
for i in t_shirt:
    bio = i%T
    if bio == 0:
        a = i//T
        count +=a
    elif bio > 0:
        count = count + (i//T) + 1

# p 구하기 나머지 와 몫
number = sum(t_shirt)
mok = number//P
remain = number%P

print(count)
print(f'{mok} {remain}')

