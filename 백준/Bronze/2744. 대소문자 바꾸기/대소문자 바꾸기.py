n = str(input())
s = []
for i in n:
    if i == i.upper():
        s.append(i.lower())
    else:
        s.append(i.upper())
k = ''
for i in range(len(n)):
    k += s[i]

print(k)



