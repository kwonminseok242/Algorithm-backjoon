def solution(sides):
    long = max(sides)
    sides.remove(long)
    if sum(sides) <= long:
        answer =2
    else:
        answer =1
    return answer