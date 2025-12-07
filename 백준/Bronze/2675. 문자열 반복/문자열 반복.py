N = int(input())

for _ in range(N):
    answer = ''
    mylist = input().split()
    number = int(mylist[0])
    string = mylist[1]

    for x in range(len(string)):
        answer += string[x] * number

    print(answer)