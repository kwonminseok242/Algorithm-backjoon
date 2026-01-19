def solution(n, k):
    s = n//10
    k = k - s 
    answer = n*12000 + k*2000
    return answer