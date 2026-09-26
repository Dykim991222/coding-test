def solution(myString, pat):
    a,b = '',''
    a += myString.lower()
    b += pat.lower()
    if b in a:
        return 1
    return 0