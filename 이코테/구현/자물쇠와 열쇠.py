def turnRight(a):
    row = len(a) # 행
    column = len(a[0]) # 열
    result = [[0] * row for _ in range(column)]
    for i in range(row):
        for j in range(column):
            result[j][row - i - 1] = a[i][j]
    return result


def check(newLock):
    lockLength = len(newLock) // 3
    for i in range(lockLength, lockLength * 2):    
        for j in range(lockLength, lockLength * 2):
            if newLock[i][j] != 1:               
                return False
    return True       


def solution(key, lock):
    N = len(lock)
    M = len(key)
    newLock = [[0] * (N * 3) for _ in range(N * 3)] # 3배
    
    for i in range(N):
        for j in range(N):
            newLock[i + N][j + N] = lock[i][j] # 기존값 입력
            
    for rotation in range(4):
        key = turnRight(key)

        for x in range(N * 2):
            for y in range(N * 2):
                
                for i in range(M): # 자물쇠에 열쇠를 끼워 넣기
                    for j in range(M):
                        newLock[x + i][y + j] += key[i][j]
                        
                if check(newLock) == True: # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                    return True
                
                for i in range(M): # 자물쇠에서 열쇠를 다시 빼기
                    for j in range(M):
                        newLock[x + i][y + j] -= key[i][j]        
    return False
