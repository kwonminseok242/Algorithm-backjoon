import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
#input()보다 sys.stdin.readline()이 빠른이유는
#sys.stdin.readline()은 C 레벨에서 한 줄을 통째로 읽어서 바로 반환한다.
#개행 문자(\n)까지 그대로 포함되므로, 문자열을 다룰 때는 보통 .rstrip()으로 잘라줌
#BOJ 기준 (입력 100만 줄):
#input() 사용: 시간 초과(TLE)
#sys.stdin.readline() 사용: 약 1~2초 내에 통과
#sys.stdin.readline() + sys.stdout.write(): 추가로 0.3~0.5초 더 빨라짐