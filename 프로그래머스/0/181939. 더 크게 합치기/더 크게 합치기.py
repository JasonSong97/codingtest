def solution(a, b):
    answer = 0
    temp1 = str(a) + str(b)
    temp2 = str(b) + str(a)
    
    if int(temp1) > int(temp2):
        return int(temp1)
    elif int(temp1) < int(temp2):
        return int(temp2)
    else:
        return int(temp1)