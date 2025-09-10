# 9x9 행렬 입력
A = [list(map(int, input().split())) for _ in range(9)]

max_val = -1         # 최댓값 초기화 (충분히 작은 값)
max_row, max_col = 0, 0   # 위치 초기화

# 모든 원소 탐색
for i in range(9):
    for j in range(9):
        if A[i][j] > max_val:
            max_val = A[i][j]
            max_row, max_col = i, j

# 출력 (행과 열은 1부터 시작하므로 +1)
print(max_val)
print(max_row+1, max_col+1)
