import sys

input = sys.stdin.readline

answer_list = []
for _ in range(10):
    N = int(input())
    answer_list.append(N%42)

answer_set = set(answer_list)
print(len(answer_set))