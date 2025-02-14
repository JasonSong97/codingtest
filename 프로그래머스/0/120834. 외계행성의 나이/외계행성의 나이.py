def solution(age):
    answer = ''
    for a in str(age):
        answer += chr(int(a) + 97)
    return answer