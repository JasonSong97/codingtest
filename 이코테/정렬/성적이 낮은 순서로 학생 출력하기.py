import sys

input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda x:x[1])
for student in array:
    print(student[0], end = " ")