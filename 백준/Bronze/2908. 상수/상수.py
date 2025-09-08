a, b = input().split()   # 문자열 그대로 받기

c = int(a[::-1])         # 문자열 뒤집어서 정수 변환
d = int(b[::-1])

print(max(c, d))
