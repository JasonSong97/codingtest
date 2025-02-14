def solution(rny_string):
    answer = ''
    for s in rny_string:
        if s == 'm':
            answer += 'rn'
        else:
            answer += s
    return answer