def solution(myString, pat):
    answer = 0
    newString = myString.lower()
    newPat = pat.lower()
    
    if newPat in newString:
        return 1
    else:
        return 0