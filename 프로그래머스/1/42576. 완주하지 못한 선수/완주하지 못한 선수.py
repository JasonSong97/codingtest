def solution(participant, completion):
    answer = ''
    
    
    m = {}
    for i in range(len(participant)):
        m[participant[i]] = 0
    for i in range(len(participant)):
        m[participant[i]] += 1
        
    
    for c in completion:
        m[c] -= 1
    for k, v in m.items():
        if v != 0:
            answer += k

    return answer