numbers = [2,3,4,5,6,7,8,9,10]

def solution(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        
    answer = sum/len(numbers)
    return answer

solution(numbers)