# 피자 나눠먹기(3)
# 조각  인원   출력
#  7   10  |  2
#  4   12  |  3
# slice = 7
# n = 10

def solution(slice, n):
    mok = n//slice
    a = mok*slice
    if a >= n:
        answer = mok
    else:
        answer = mok+1
    return answer

