def solution(a, b):
    answer = 0
    temp1 = int(str(a) + str(b))
    temp2 = int(str(b) + str(a))
    if temp1 > temp2:
        return temp1
    elif temp1 < temp2:
        return temp2
    else:
        return temp1