def solution(num_list):
    answer = []
    for n in num_list:
        answer.append(n)
    
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    elif num_list[-1] <= num_list[-2]:
        answer.append(num_list[-1] * 2)
        
    return answer