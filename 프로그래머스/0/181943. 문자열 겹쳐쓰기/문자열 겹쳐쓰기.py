def solution(my_string, overwrite_string, s):
    # answer = my_string.replace(my_string[s: s + len(overwrite_string)], overwrite_string)
    answer = ''
    myStringData = list(my_string)
    overWriteString = list(overwrite_string)
    for i in range(len(overWriteString)):
        myStringData[s + i] = overWriteString[i]
    
    
    
    return answer.join(myStringData)