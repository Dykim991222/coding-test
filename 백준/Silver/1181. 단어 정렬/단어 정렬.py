import sys
input = sys.stdin.readline

N = int(input())
word_list = []
for _ in range(N):
    word = input().strip()
    word_list.append(word)

non_duplicate_list = list(set(word_list))

non_duplicate_list.sort()
non_duplicate_list.sort(key=len)

for i in range(len(non_duplicate_list)):
    print(non_duplicate_list[i])