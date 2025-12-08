import sys
input = sys.stdin.readline

# strfry 함수? : 입력된 문자열을 무작위로 재배열, 새로운 문자열 만들어냄. 
# 2개의 문자열에 대해 2번째 문자열이 1번째 문자열에 strfry함수를 적용하여 얻어질수있니

N = int(input())
answer = []
for _ in range(N):
    sent1, sent2 = map(str, input().split())
    if sorted(sent1) == sorted(sent2):
        answer.append('Possible')
    else:
        answer.append('Impossible')

for i in range(len(answer)):
    print(answer[i])