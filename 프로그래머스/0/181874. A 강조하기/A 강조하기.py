def solution(myString):
    answer = ''
    for s in myString:
        if s == 'a':
            answer += 'A'
        elif s == 'A':
            answer += s
        else:
            answer += s.lower()
    return answer