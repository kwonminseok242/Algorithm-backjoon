students = set(range(1, 31))  # 1~30번 학생 전체 집합

for _ in range(28):
    n = int(input())
    students.remove(n)  # 제출한 학생 제거

# 남은 학생 번호 정렬해서 출력
for s in sorted(students):
    print(s)