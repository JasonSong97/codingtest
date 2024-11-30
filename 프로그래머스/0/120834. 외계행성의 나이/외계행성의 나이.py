def solution(age):
    answer = ''
    alpha = ['a', 'b', 'c' ,'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    strAge = str(age)
    for s in strAge:
        for i in range(len(s)):
            answer += alpha[int(s[i])]
    return answer