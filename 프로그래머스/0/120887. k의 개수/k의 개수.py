def solution(i, j, k):
    answer = 0
    for i in range(i, j + 1):
        strNum = list(str(i))
        for n in range(len(strNum)):
            if strNum[n] == str(k):
                answer += 1
    return answer