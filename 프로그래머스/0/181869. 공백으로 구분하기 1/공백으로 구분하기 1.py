def solution(my_string):
    answer = []
    temp = ''
    for s in my_string:
        if s == ' ':
            if temp == '':
                continue
            else:
                answer.append(temp)
                temp = ''
        else:
            temp += s
    if temp != '':
        answer.append(temp)
    return answer