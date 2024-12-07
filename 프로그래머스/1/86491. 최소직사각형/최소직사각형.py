# 한쪽이 모두 커야 함

def solution(sizes):
    answer = 0
    xDataList = []
    yDataList = []
    for s in sizes:
        x = s[0]
        y = s[1]
        if x < y:
            temp = x
            x = y
            y = temp
        xDataList.append(x)
        yDataList.append(y)
    
        
    return max(xDataList) * max(yDataList)