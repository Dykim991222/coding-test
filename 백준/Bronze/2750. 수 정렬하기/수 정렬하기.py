import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = []
for _ in range(N):
    x = int(input().rstrip())
    numbers.append(x)

numbers.sort()

for i in range(N):
    print(numbers[i])