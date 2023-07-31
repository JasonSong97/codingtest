import sys

input = sys.stdin.readline

S = input().strip()

count1 = 0
count0 = 0

if S[0] == '1':
  count0 += 1  # 0
else:
  count1 += 1  # 1

for i in range(len(S) - 1): # 6
  if S[i] != S[i + 1]:
    if S[i + 1] == '1':
      count0 += 1
    else:
      count1 += 1

print(min(count1, count0))
