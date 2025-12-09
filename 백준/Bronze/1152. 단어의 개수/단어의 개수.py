import sys
input = sys.stdin.readline

'''
input = 영어 대소문자와 공백으로 이루어진 문자열
이 문자열에는 몇개의 단어?
한 단어가 여러번 등장하면 등장한 횟수만큼 세어라
'''

sentence = list(map(str, input().split()))
answer = len(sentence)
print(answer)