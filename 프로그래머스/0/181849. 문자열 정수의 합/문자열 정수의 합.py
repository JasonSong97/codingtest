def solution(num_str):
    answer = 0
    for n in num_str:
        temp = int(n)
        answer += temp
    return answer