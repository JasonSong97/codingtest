def solution(order):
    answer = 0
    for o in order:
        if 'latte' in o:
            answer += 5000
        elif 'americano' in o:
            answer += 4500
        else:
            answer += 4500
    return answer