def solution(array, n):
    answer = 0
    for a in array:
        if a == n:
            answer += 1
    return answer