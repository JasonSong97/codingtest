def solution(num_list):
    mu = []
    m = 1
    for n in num_list:
        m = m * n
    
    a = sum(num_list)
    s = a * a
    if m > s:
        return 0
    else:
        return 1