import sys

input = sys.stdin.readline

S = input()
data = [0] * 26

for i in range(len(S) - 1):
  data[ord(S[i]) - 97] += 1

for i in range(len(data)):
  print(data[i], end=" ")
