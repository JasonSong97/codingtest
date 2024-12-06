def solution(my_str, n):
    answer = []
    
    temp = ''
    count = 0
    for i in range(len(my_str)):
        count += 1
        temp += my_str[i]
        if count == n:
            answer.append(temp)
            temp = ''
            count = 0
    if count != 0:
        answer.append(temp)
    
    return answer