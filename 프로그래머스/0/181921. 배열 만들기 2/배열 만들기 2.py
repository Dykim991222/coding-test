def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if i % 5 == 0:      
            answer.append(i)

    new_answer = []
    for x in answer:
        ok = True
        for ch in str(x):
            if ch not in ('0', '5'):
                ok = False
                break
        if ok:
            new_answer.append(x)
            
    

    return new_answer if new_answer else [-1]
