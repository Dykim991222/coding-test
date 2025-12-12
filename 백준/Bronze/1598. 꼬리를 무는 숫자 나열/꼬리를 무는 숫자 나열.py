import sys
input = sys.stdin.readline
'''
입력받은거 기반 큰수로 이중for문 -> 리스트만들기


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

(r1, c1), (r2, c2) = answer_list
print(abs(r1 - r2) + abs(c1 - c2))
'''
A, B = map(int, input().split()) # 11, 33
A -= 1
B -= 1

r1, c1 = A // 4, A % 4
r2, c2 = B // 4, B % 4

print(abs(r1 - r2) + abs(c1 - c2))
