def solution(rsp):
    answer = ''
    for t in rsp:
        if t == '2':
            answer += '0'
        elif t == '0':
            answer += '5'
        else:
            answer += '2'
            
    return answer