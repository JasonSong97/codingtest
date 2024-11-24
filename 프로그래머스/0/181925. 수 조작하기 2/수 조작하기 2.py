def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        minus = numLog[i] - numLog[i - 1]
        if minus == 1:
            answer += 'w'
        elif minus == -1:
            answer += 's'
        elif minus == 10:
            answer += 'd'
        elif minus == -10:
            answer += 'a'
    return answer