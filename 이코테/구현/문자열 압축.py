# 푼 날짜
# 2023/8/27

def solution(s): # abcabcdede
    answer = len(s)  # 10
    
    for compressionLevel in range(1, (len(s) // 2) + 1):
        compress = ""
        previous = s[0 : compressionLevel] 
        sameLetterCount = 1
        
        for i in range(compressionLevel, len(s), compressionLevel):
            
            if previous == s[i : i + compressionLevel]: # 같으면
                sameLetterCount += 1
            else: # 같지 않다면
                if sameLetterCount == 1:
                    compress += previous
                else:
                    compress += str(sameLetterCount) + previous
                
                # 초기화
                previous = s[i : i + compressionLevel]
                sameLetterCount = 1
        
        # 남이있는 문자열 처리(홀수 일 경우)
        if sameLetterCount == 1:
            compress += previous
        else:
            compress += str(sameLetterCount) + previous
        
        answer = min(answer, len(compress))
    return answer