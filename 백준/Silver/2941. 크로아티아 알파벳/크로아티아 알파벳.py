import sys
input = sys.stdin.readline

'''
크로아티아 알파벳을 입력할수가 없음
1. 크로아티아 알파벳 리스트 만들고
2. 이 리스트 돌면서 감지되면 그냥 임의의 뭔가로 바꿔버릴래
'''
word = input().rstrip()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for alpha in croatia:
    word = word.replace(alpha, '@')

print(len(word))