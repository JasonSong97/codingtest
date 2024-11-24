def solution(n):
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        adj[i][i] = 1
    return adj