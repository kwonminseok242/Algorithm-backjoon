word = input().upper()  # 대소문자 구분 안 하도록 전부 대문자 변환
unique = list(set(word))  # 중복 제거된 알파벳 집합

cnts = []
for ch in unique:
    cnts.append(word.count(ch))

if cnts.count(max(cnts)) > 1:
    print("?")
else:
    print(unique[cnts.index(max(cnts))])
