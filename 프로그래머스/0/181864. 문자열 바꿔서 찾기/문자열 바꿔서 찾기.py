def solution(myString, pat):
    temp = ''
    for s in myString:
        if s == 'A':
            temp += 'B'
        else:
            temp += 'A'
    
    if pat in temp:
        return 1
    else:
        return 0