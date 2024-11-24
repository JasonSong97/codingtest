def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        t = int("".join(intStrs[i][s: s + l]))
        if t > k:
            answer.append(t)
    return answer