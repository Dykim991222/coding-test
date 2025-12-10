import sys
input = sys.stdin.readline
'''
9개의 서로 다른 자연수 들어옴
최댓값은 몇번째 수?
1. for문 돌면서 max보다 크면 index를 max에 저장
'''

num_list = []
for _ in range(9):
    num = int(input())
    num_list.append(num)

max = 0
answer = 0

for i in range(9):
    if num_list[i] > max:
        max = num_list[i]
        answer = i

print(max)
print(answer+1)