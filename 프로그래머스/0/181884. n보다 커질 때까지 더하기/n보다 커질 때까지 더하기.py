def solution(numbers, n):
    answer = 0
    
    for x in numbers:
        answer += x
        if answer > n:
            return answer
    
    return answer