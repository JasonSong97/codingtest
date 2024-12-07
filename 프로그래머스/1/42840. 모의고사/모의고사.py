def solution(answers):
    answer = []
    tempCount = 0
    
    oneSupo = [1, 2, 3, 4, 5]
    for i in range(len(answers)):
        idx = i
        if idx >= 5:
            idx %= 5
        if answers[i] == oneSupo[idx]:
            tempCount += 1
    answer.append((tempCount, 1))
        
    tempCount = 0
    twoSupo = [2, 1, 2, 3, 2, 4, 2, 5]
    for i in range(len(answers)):
        idx = i
        if idx >= 8:
            idx %= 8
        if answers[i] == twoSupo[idx]:
            tempCount += 1
    answer.append((tempCount, 2))
    
    tempCount = 0
    threeSupo = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        idx = i
        if idx >= 10:
            idx %= 10
        if answers[i] == threeSupo[idx]:
            tempCount += 1
            
    answer.append((tempCount, 3))
    
    answer.sort(key = lambda x: (-x[0], x[1]))
    firstValueList = [answer[i][0] for i in range(3)]
    maxData = max(firstValueList)
    
    temp = []
    for i in range(len(answer)):
        if answer[i][0] == maxData:
            temp.append(answer[i][1])
            
        
    
    return temp