def solution(num_list):
    
    even_sum = ''
    odd_sum = ''
    for n in num_list:
        if n % 2 == 0:
            even_sum += str(n)
        else:
            odd_sum += str(n)
    return int(even_sum) + int(odd_sum)