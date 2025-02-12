def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
        else:
            continue
    return answer