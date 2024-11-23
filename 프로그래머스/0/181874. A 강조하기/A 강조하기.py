def solution(myString):
    answer = ''
    for s in myString:
        if s == 'a':
            answer += s.upper()
            
        elif s == 'A':
            answer += s
        else:
            if s == ' ':
                answer += s
            else:
                answer += s.lower()
    return answer