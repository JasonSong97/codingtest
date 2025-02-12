def solution(n):
    count = n % 7
    if count == 0:
        return n // 7
    else:
        return (n // 7) + 1