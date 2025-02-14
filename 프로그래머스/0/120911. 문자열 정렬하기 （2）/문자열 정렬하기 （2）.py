def solution(my_string):
    answer = []
    for s in my_string:
        answer.append(s.lower())
    answer.sort()
    result = ''
    for a in answer:
        result += a
    
    return result