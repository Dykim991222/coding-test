import sys
input = sys.stdin.readline
'''
기말고사 점수 중 최댓값 = M
모든 점수들을 점수/70*100
시험 본 과목의 개수 = N
'''
N = int(input())
scores = list(map(int, input().split(' ')))

M = 0
for i in range(N):
    if scores[i] > M:
        M = scores[i]

answer = 0
for score in scores:
    answer += (score / M * 100)

print(answer/N)