a, b, v = map(int, input().split())

A = a-b
V = v-b

if V%A == 0:
    print(int(V/A))
else:
    print(int(V//A+1))