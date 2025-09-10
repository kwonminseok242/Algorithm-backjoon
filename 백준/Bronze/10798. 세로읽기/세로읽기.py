lines = [input().rstrip() for _ in range(5)]  # 5줄 입력

result = ""

# 가장 긴 줄 길이만큼 열 인덱스를 돌기
max_len = max(len(line) for line in lines)

for i in range(max_len):     # 열
    for j in range(5):       # 행
        if i < len(lines[j]):   # 해당 줄에 그 열 문자가 있으면
            result += lines[j][i]

print(result)
####어렵다####