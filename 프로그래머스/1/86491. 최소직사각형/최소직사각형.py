def solution(sizes):
    xDataList = []
    yDataList = []
    
    for size in sizes:
        if size[0] < size[1]:
            xDataList.append(size[1])
            yDataList.append(size[0])
        else:
            xDataList.append(size[0])
            yDataList.append(size[1])
    
    return max(xDataList) * max(yDataList)