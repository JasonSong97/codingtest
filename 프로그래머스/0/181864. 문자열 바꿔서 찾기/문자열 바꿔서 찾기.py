def solution(myString, pat):
    answer = ''
    for s in myString:
        if s == 'A':
            answer += "B"
        else:
            answer += "A"
    
    return 1 if pat in answer else 0 