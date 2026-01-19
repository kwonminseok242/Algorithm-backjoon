
def solution(my_string):
    str1 = list(my_string)
    str1 = list(reversed(str1))
    a = ''
    for i in range(len(str1)):
        a += str1[i]
    a
    return a