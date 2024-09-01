# 아이디어 1) 0 <= n <= 40 2) 점화식 3) 재귀는 실패
# 자료구조 dp
# 시간복잡도 0.25초
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    temp = int(input())

    # dp 구성하기
    dp = [[]] * 41 # 0 <= temp <= 40
    dp[0] = [1, 0] # 0의 0 개수와 1개수 넣기
    dp[1] = [0, 1] # 1의 0개수와 1개수 넣기
    dp[2] = [1, 1] # 2의 0개수와 1개수 넣기

    # dp[n] = [dp[n - 1][0] + dp[n - 2][0], dp[n - 1][1] + dp[n - 2][1]]
    
    # 앞에 3개를 제외한 나머지 전부 dp에 넣기
    for i in range(3, 41):
        dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

    print(dp[temp][0], dp[temp][1])