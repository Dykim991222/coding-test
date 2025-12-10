import sys
input = sys.stdin.readline
'''
일단 A. B, C 입력받고 결과값만 사용.
결과값을 문자열로 변환하고 하나씩 받아오자.
10개의 0으로 구성된 리스트에 for문으로 결과값 돌면서
1씩더하는방식 
'''
A = int(input())
B = int(input())
C = int(input())
result = A * B * C

str_result = str(result)
num_list = [0 for _ in range(10)]

for single_num in str_result:
    num_list[int(single_num)] += 1

for num in num_list:
    print(num)
    