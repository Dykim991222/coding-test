S = list(input())
abc = 'abcdefghijklmnopqrstuvwxyz'
abc_list = list(abc)

for a in abc:
    if a in S:
        print(S.index(a), end = ' ')
    else:
        print(-1, end = ' ')