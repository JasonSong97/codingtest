import math

def solution(brown, yellow):
    answer = []
    pointList = []
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            pointList.append((yellow // i, i))
        else:
            continue
    for point in pointList:
        garo = point[0] + 2
        sero = point[1] + 2
        
        if (garo * sero) == (brown + yellow):
            return [garo, sero]