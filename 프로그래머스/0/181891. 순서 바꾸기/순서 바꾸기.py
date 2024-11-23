def solution(num_list, n):
    answer = []
    first = num_list[n: ]
    second = num_list[: n]
    for f in first:
        answer.append(f)
    for s in second:
        answer.append(s)
    return answer