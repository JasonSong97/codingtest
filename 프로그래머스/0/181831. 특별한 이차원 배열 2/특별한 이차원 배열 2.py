def solution(arr):
    answer = 0
    for row in range(len(arr)):
        for column in range(len(arr)):
            if arr[row][column] != arr[column][row]:
                return 0
    
    return 1