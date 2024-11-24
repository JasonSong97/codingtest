def solution(number):
    strNumber = str(number)
    tempSum = 0
    for s in strNumber:
        tempSum += int(s)
    rest = tempSum % 9
    return rest