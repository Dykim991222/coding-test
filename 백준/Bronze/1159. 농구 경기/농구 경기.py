import sys
input = sys.stdin.readline

'''
상근이는 감독, 내일 경기에 나설 선발명단 필
선수이름 기억못하고, 능력도 알지못함
1. 성의 첫글자가 같은 선수 5명 그냥 뽑을거
2. if len(성의 첫글자가 같은 선수) < 5:
    return PREDAJA
3. 첫줄은 숫자입력받고, 그만큼 선수이름 입력받을거임
'''

N = int(input())
count = {}

for _ in range(N):
    name = input().strip()
    first = name[0]

    if first in count:
        count[first] += 1
    else:
        count[first] = 1

result = [ch for ch, cnt in count.items() if cnt >= 5]

if not result:
    print('PREDAJA')
else:
    result.sort()
    print(''.join(result))

