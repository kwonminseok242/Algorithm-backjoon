a,b,c = map(int,input().split())
# 삼각형 각 길이 리스트 만들기
triangle = [a,b,c]
# 가장 큰 변 찾기
max_len = max(triangle)
# 가장 큰 변 빼고 남기기
triangle.remove(max_len)

if sum(triangle) > max_len:
    print(sum(triangle)+ max_len)
elif sum(triangle)==max_len:
    print(sum(triangle)+max_len-1)
elif sum(triangle) < max_len:
    print(sum(triangle)+(sum(triangle)-1))