def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        candidates = []
        for i in range(s, e+1):
            if arr[i] > k:
                candidates.append(arr[i])
        
        if candidates:
            answer.append(min(candidates))
        else:
            answer.append(-1)
    return answer
