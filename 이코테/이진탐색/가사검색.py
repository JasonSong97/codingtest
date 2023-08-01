# 풀이방법

# 1. words -> 사이즈별로 분리
# 2. 사이즈별로 분리 후, 이진탐색을 위한 정렬
# 3. bisect 라이브러리 이용해서 범위의 개수 구하기

from bisect import bisect_left, bisect_right

def countByRange(array, leftValue, rightValue):
    leftIndex = bisect_left(array, leftValue)
    rightIndex = bisect_right(array, rightValue)
    return rightIndex - leftIndex

# 키워드의 사이즈 리스트에 넣기
data = [[] for _ in range(10001)] 
reverseData = [[] for _ in range(10001)] # ????o 해결용 -> 뒤집어서 해결

def solution(words, queries):
    answer = []
    
    for word in words:
        data[len(word)].append(word)
        reverseData[len(word)].append(word[ : : -1]) # 뒤집기
        
    for i in range(10001): # 이진탐색을 위한 사이즈별 정렬
        data[i].sort() 
        reverseData[i].sort()
        
    for query in queries:
        if query[0] != '?':
            result = countByRange(data[len(query)], 
                         query.replace('?', 'a'), 
                         query.replace('?', 'z'))
        else:
            result = countByRange(reverseData[len(query)], 
                         query[ : : -1].replace('?', 'a'), 
                         query[ : : -1].replace('?', 'z'))
        answer.append(result)
    
    return answer