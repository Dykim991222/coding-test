def solution(arr, queries):
    answer = []
    for query in queries:
        k = 0
        k = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = k
    return arr