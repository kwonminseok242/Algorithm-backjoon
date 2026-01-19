def solution(n):
    if n%7 == 0:
        k = n/7
        answer = k
    else:
        answer = n//7 +1
    return answer