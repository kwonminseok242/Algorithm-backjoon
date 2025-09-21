x, y, w, h = map(int, input().split())

# 4방향 거리 중 최솟값을 출력
print(min(x, y, w - x, h - y))
