def solution(num_list):
    answer = 0
    numTotal = sum(num_list) * sum(num_list)
    multiTotal = 1
    for n in num_list:
        multiTotal *= n
    return 1 if numTotal > multiTotal else 0