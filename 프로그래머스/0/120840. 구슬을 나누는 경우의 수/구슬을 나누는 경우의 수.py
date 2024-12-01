from itertools import combinations

def solution(balls, share):
    up = 1
    for i in range(1, balls + 1):
        up *= i
    
    bottomLeft = 1
    for i in range(1, balls - share + 1):
        bottomLeft *= i
    bottomRight = 1
    for i in range(1, share + 1):
        bottomRight *= i
    
    
    return up / (bottomLeft * bottomRight)