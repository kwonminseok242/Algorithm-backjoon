n = int(input())
score = list(map(int, input().split()))

m = max(score)  # 최고점
new_scores = [(s / m) * 100 for s in score]  # 점수 변환

print(sum(new_scores) / n)
