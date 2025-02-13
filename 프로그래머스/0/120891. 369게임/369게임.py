def solution(order):
    a = ['3', '6','9']
    answer = 0
    for i in str(order):
        if i in a:
            answer += 1
    return answer