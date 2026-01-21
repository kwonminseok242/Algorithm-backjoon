c,d,e,f,g,a,b,p = map(int, input().split())
input_1 = [c-1,d-1,e-1,f-1,g-1,a-1,b-1,p-1] # 1,2,4,5,6,7,8
         # 0    1   2   3   4   5   6   7
# print(f'input_1 : {input_1}')      
de = list(reversed(input_1))

result = ""

if c == 1 and p == 8:
    result = "ascending"
    for i in range(8):
        if input_1[i] != i:
            result = "mixed"
            break # 하나라도 틀리면 바로 탈출
            
elif c == 8 and p == 1:
    result = "descending"
    for i in range(8):
        if de[i] != i:
            result = "mixed"
            break
            
else:
    result = "mixed"

print(result)