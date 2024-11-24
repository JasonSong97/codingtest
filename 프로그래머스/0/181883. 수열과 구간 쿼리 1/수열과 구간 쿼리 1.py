def solution(arr, queries):
    for i in range(len(queries)):
        for j in range(queries[i][0], queries[i][1] + 1):
            arr[j] += 1
    return arr

# 0 1 2 3 4
# 1 2 2 3 4
# 1 3 3 3 4
# 1 3 4 4 4