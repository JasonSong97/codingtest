# 푼 날짜
# 2023/8/27

N = str(int(input()))

length = len(N)
leftSum = 0
rightSum = 0
for i in range(length // 2):
     leftSum += int(N[i])

for i in range(length // 2, length):
     rightSum += int(N[i])

if leftSum == rightSum:
     print("LUCKY")
else:
     print("READY")