def solution(num_list):
    answer = 0
    oddSum = ""
    evenSum = ""
    for n in num_list:
        if n % 2 == 0:
            evenSum += str(n)
        else:
            oddSum += str(n)
    return int(evenSum) + int(oddSum)