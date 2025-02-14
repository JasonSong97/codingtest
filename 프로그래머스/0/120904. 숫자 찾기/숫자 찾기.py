def solution(num, k):
    if str(k) not in str(num):
        return -1
    else:
        for i in range(len(str(num))):
            if str(num)[i] == str(k):
                return i + 1