def solution(myString):
    answer = ''
    for s in myString:
        if ord(s) >= 108:
            answer += s
        else:
            answer += "l"
            
    return answer

# a 97 -> l 108