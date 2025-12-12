import sys
input = sys.stdin.readline
'''
입력받은거 기반 큰수로 이중for문 -> 리스트만들기
'''

A, B = map(int, input().split(' '))
small, big = min(A,B) , max(A,B)
mylist = []
for i in range(1, big//4+2):
    mylist.append([(i*4-3),(i*4-2),(i*4-1),(i*4)])

answer_list = []
for i in range(big//4+1):
    for k in range(4):
        if mylist[i][k] == small:
            answer_list.append([i, k])
        if mylist[i][k] == big:
            answer_list.append([i, k])

print(answer_list)