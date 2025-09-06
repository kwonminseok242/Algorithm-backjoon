N = int(input())                 # 정수의 개수
numbers = list(map(int, input().split()))  # 정수 리스트
v = int(input())                 # 찾으려는 정수

# 개수 세기
count = numbers.count(v)

# 결과 출력
print(count)