def solution(hp):
    answer = 0
    t = [5, 3, 1]
    
    for i in t:
        answer = answer + (hp // i)
        hp = hp % i
    
    return answer