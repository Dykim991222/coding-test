import sys

input = sys.stdin.readline

number_list = [[2,'abc'],
               [3,'def'],
               [4,'ghi'],
               [5,'jkl'],
               [6,'mno'],
               [7,'pqrs'],
               [8,'tuv'],
               [9,'wxyz']]

answer = 0
string = input().strip().lower()
for x in string:
    for num, alpha in number_list:
        if x in alpha:
            answer += num + 1

print(answer)