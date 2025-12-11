import sys
input = sys.stdin.readline

N = str(input().strip())
mylist = []
for number in N:
    mylist.append(int(number))

answer = sorted(mylist, reverse=True)
for i in range(len(answer)):
    print(answer[i], end='')