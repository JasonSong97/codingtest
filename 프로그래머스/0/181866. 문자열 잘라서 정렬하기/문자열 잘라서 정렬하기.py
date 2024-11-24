def solution(myString):
    temp = myString.split("x")
    answer = []
    for t in temp:
        if t != '':
            answer.append(t)
    
    return sorted(answer)