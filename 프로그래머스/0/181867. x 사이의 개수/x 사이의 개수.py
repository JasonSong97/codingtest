def solution(myString):
    answer = []
    tempData = list(myString.split('x'))
    for t in tempData:
        answer.append(len(t))
    return answer