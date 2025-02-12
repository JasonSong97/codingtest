def solution(my_string):
    answer = ''
    t = ['a','e','i','o','u']
    for s in my_string:
        if s in t:
            continue
        else:
            answer += s
    return answer