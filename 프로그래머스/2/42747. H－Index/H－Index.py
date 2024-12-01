def solution(citations):
    answer = 0
    citations.sort()
    
    for tempHIndex in range(1, len(citations) + 1): # 1 ~ 5
        overCount = 0
        for c in citations: # [0, 1, 3, 5, 6]
            if c >= tempHIndex:
                overCount += 1
        
        if tempHIndex <= overCount:
            answer = max(answer, tempHIndex)
    
    return answer
