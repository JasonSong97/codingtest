def solution(my_string, n):
    answer = ''
    for s in my_string:
        for _ in range(n):
            answer += s
    return answer