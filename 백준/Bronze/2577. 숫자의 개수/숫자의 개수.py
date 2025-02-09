import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

temp = a * b * c
strTemp = str(temp)
data = [0] * 10
for s in strTemp:
    data[int(s)] += 1
for i in range(len(data)):
    print(data[i])