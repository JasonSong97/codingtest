# 1
def solution(N, stages):
    # [2, 1, 2, 6, 2, 4, 3, 3]
    length = len(stages)
    failList = []
    
    for level in range(1, N + 1): # 1, 2, 3, 4, 5
        failCount = 0
        
        for person in stages:
            # [1, 2, 2, 2, 3, 3, 4, 6]
            if person == level:
                failCount += 1
            else:
                continue 
        # 각 level에 대한 실패수 존재
        failRate = 0
        if failCount >= 1:
            failRate = failCount / length
            length -= failCount
            failCount = 0
        else:
            failRate = 0
        
        failList.append((failRate, level))
        
    failList.sort(key = lambda x: x[0], reverse = True)
    
    answer = []
    for i in range(N):
        answer.append(failList[i][1])
    return answer

# 2
def solution2(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= 1
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]

    return answer