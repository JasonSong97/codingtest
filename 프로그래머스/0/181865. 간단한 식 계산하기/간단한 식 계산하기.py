def solution(binomial):
    answer = 0
    
    tempData = list(binomial.split(" "))
    if tempData[1] == '+':
        answer = int(tempData[0]) + int(tempData[2])
    elif tempData[1] == '-':
        answer = int(tempData[0]) - int(tempData[2])
    else:
        answer = int(tempData[0]) * int(tempData[2])
    return answer