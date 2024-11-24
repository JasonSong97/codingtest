def solution(my_string, s, e):
    answer = my_string[: s] # Progra
    
    temp = my_string[s: e + 1]
    
    t = ''
    for i in range(len(temp)):
        t += temp[e - s - i]
    print(t)
    
    answer += t
    answer += my_string[e + 1: ]
    return answer

# Progra21Sremm3 -> 21Sremm