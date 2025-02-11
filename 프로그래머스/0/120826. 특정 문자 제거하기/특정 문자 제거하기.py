def solution(my_string, letter):
    answer = ''
    for i in range(len(my_string)):
        if letter == my_string[i]:
            continue
        else:
            answer += my_string[i]
    return answer