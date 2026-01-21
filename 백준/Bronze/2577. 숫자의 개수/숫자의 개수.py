# 2577번 숫자의 개수
# 처음 든 생각으로는 반복문일까? 생각했지만 곱하기여서 숫자가 너무 크면 반복이 무한이 될꺼같아서
# If문 도배를 해야겠다고 생각이 든다.

k = int(input())
m = int(input())
n = int(input())
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
p = 0
j = 0


num = str(k*m*n)
for i in num:
    if str(i) == '0':
        a += 1
    elif str(i) == '1':
        b += 1
    elif str(i) == '2':
        c += 1
    elif str(i) == '3':
        d += 1
    elif str(i) == '4':
        e += 1
    elif str(i) == '5':
        f += 1
    elif str(i) == '6':
        g += 1
    elif str(i) == '7':
        h += 1
    elif str(i) == '8':
        p += 1
    else:
        j += 1

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(p)
print(j)