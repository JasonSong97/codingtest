def solution(s): # abcabcdede
    answer = len(s)  # 10
    
    for step in range(1, answer // 2 + 1): # 1, 2, 3, 4, 5
        compressed = ""
        prev = s[0 : step] 
        count = 1
        
        for j in range(step, len(s), step):
            if prev == s[j : j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]
                count = 1
                
        compressed += str(count) + prev if count >= 2 else prev
        
        answer = min(answer, len(compressed))
    return answer