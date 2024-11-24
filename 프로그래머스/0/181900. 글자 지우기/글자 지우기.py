def solution(my_string, indices):
    answer = ''
    temp = list(my_string)
    for i in indices:
        temp[i] = ''
    for t in temp:
        answer += t
    return answer