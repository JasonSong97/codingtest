def solution(num_list):
    answer = []
    oddCount = 0
    evenCount = 0
    for n in num_list:
        if n % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    return [evenCount, oddCount]