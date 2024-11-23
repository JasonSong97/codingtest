def solution(num_list):
    oddSum = 0
    evenSum = 0
    
    for i in range(len(num_list)):
        if (i + 1) % 2 == 0:
            oddSum += num_list[i]
        else:
            evenSum += num_list[i]
    return max(oddSum, evenSum)