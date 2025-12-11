import sys
input = sys.stdin.readline
'''
알파뱃 대소문자로 된 단어 -> 소문자로 바꾸고
가장 많이 사용된거 찾아줘
'''
cnt = {}
word = input().strip()
for alpha in word:
    a = alpha.lower()
    if a not in cnt:
        cnt[a] = 1
    else:
        cnt[a] += 1

max_count = max(cnt.values())
mylist = []
result = 0
for a, b in cnt.items():
    if b == max_count:
        result += 1
        mylist.append(a)

if result == 1:
    print(mylist[0].upper())
else:
    print('?')

