import sys
input = sys.stdin.readline
'''
1. 숫자입력받고
2. join으로 쪼개서 리스트
3. flag = true 잡고
4. 리스트안에 없거나 전에 나왔었으면 그대로 가고
5. 아니면 flag = False
6. if flag = False : cnt += 1
'''
def check_group_words(word):
    seen = set()
    prev = ''

    for ch in word:
        if ch != prev and ch in seen:
            return 0
        seen.add(ch)
        prev = ch
    
    return 1

N = int(input())
words = []
answer = 0

for _ in range(N):
    word = input().strip()
    words.append(word)

for word in words:
    answer += check_group_words(word)

print(answer)