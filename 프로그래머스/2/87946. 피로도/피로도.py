from itertools import permutations

def solution(pirodo, dungeons):
    answer = -1
    
    newDungeons = []
    for i in range(len(dungeons)):
        if dungeons[i][0] > pirodo:
            continue
        else:
            newDungeons.append(dungeons[i])
    
    answerList = []
    for d in permutations(newDungeons):
        visitCount = 0
        tempPirodo = pirodo
        for idx in range(len(d)):
            if tempPirodo >= d[idx][0]:
                tempPirodo -= d[idx][1]
                visitCount += 1
            else:
                continue
        answerList.append(visitCount)
    return max(answerList)