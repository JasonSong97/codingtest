import sys

input = sys.stdin.readline

now = input() # a1

row = int(now[1]) # 1 -> 1
column = ord(now[0]) - 96 # a -> 1
# a1 -> column, row 

directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

answer = 0
for direction in directions:
  nextRow = row + direction[1]
  nextColumn = column + direction[0]

  if 1 <= nextRow <= 8 and 1 <= nextColumn <= 8:
    answer += 1

print(answer)