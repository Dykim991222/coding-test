import sys

input = sys.stdin.readline

check = [False] * 31

for _ in range(28):
    x = int(input())
    if check[x] == False:
        check[x] = True

answer_list = []
for i in range(len(check)):
    if check[i] == False:
        answer_list.append(i)

print(answer_list[1])
print(answer_list[2])