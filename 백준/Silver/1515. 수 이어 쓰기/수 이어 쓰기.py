S = input().strip()

i = 0          # S에서 현재 매칭할 위치
n = 0
while i < len(S):
    n += 1
    for ch in str(n):          # n의 각 자리수를 '스트리밍'으로 흘려보냄
        if i < len(S) and ch == S[i]:
            i += 1
            if i == len(S):    # 전부 매칭되면 즉시 종료
                break

print(n)
