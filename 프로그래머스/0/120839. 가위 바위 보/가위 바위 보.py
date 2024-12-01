# 가위 2 / 바위 0 / 보 5
def solution(rsp):
    answer = ''
    for temp in rsp:
        if temp == '2':
            answer += '0'
        elif temp == '0':
            answer += '5'
        else:
            answer += '2'
    
    return answer