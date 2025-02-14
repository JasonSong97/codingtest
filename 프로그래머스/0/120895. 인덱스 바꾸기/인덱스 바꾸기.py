def solution(my_string, num1, num2):
    answer = ''
    data = list(map(str, my_string))
    temp = data[num2]
    data[num2] = data[num1]
    data[num1] = temp
    return ''.join(data)