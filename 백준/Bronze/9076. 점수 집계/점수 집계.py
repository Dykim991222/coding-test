import sys
input = sys.stdin.readline

N = int(input())
answer = []

for _ in range(N):
    my_list = list(map(int, input().split()))
    my_list.sort()
    min, max = my_list[1], my_list[3]
    if max - min >= 4:
        answer.append("KIN")
    else:
        answer.append(my_list[1] + my_list[2] + my_list[3])

for x in answer:
    print(x)

