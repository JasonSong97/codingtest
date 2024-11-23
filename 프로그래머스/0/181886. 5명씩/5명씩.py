def solution(names):
    answer = []
    
    cnt = 0
    temp = []
    for n in names:
        temp.append(n)
        if len(temp) >= 5:
            answer.append(temp[0])
            temp = []
    if len(temp) != 0:
        answer.append(temp[0])
        
    
    return answer