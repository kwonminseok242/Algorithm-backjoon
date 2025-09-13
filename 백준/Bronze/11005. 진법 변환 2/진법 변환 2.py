N, B = input().split()
N = int(N)
B = int(B)

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''

while N > 0:
    result = digits[N % B] + result
    N //= B

print(result)
