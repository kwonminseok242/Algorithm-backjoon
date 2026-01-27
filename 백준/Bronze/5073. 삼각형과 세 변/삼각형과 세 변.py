while True:
    a,b,c = map(int,input().split())
    triangle = [a,b,c]
    if triangle[0] == 0:
        break
    max_len = max(triangle)
    triangle.remove(max_len)

    if sum(triangle) > max_len:
        if a == b and b == c:
            print('Equilateral')
        elif a == b or b == c or a == c:
            print('Isosceles')
        elif a != b and b != c:      
            print('Scalene')
    else:
        print('Invalid')