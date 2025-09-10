N, M = map(int, input().split())   # 첫 줄: 행, 열 크기

A = [list(map(int, input().split())) for _ in range(N)]  # 첫 번째 행렬
B = [list(map(int, input().split())) for _ in range(N)]  # 두 번째 행렬

for i in range(N):
    row = [A[i][j] + B[i][j] for j in range(M)]  # 같은 위치 원소끼리 합
    print(*row)

####행렬 어렵다####