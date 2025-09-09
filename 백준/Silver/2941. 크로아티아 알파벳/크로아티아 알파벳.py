# 크로아티아 알파벳 리스트
arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

alpa = input().strip()

for pattern in arr:
    alpa = alpa.replace(pattern, "*")  # 크로아티아 알파벳을 *로 치환

print(len(alpa))  # 바뀐 문자열의 길이가 곧 글자 수
