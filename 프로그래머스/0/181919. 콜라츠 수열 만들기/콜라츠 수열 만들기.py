def solution(n):
    answer = []
    answer.append(n)
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        answer.append(n)
        
        
    return answer