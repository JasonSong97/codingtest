def solution(board, k):
    answer = 0
    for row in range(len(board)):
        for column in range(len(board[0])):
            if row + column <= k:
                answer += board[row][column]
    return answer