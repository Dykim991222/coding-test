import sys
input = sys.stdin.readline

# ROT13 : 영어알파벳을 13글자씩 밀어서 만듬.
# 알파벳 대문자, 소문자에만 적용
S = input()

for ch in S:
    if 'A' <= ch <= 'Z':      # 대문자
        print(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')), end='')
    elif 'a' <= ch <= 'z':    # 소문자
        print(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')), end='')
    else:                     
        print(ch, end='')

        