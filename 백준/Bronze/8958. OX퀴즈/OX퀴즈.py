import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    ans = input().strip()  
    score = 0
    cnt = 0

    for a in ans:
        if a == 'O':       
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)
