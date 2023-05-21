import sys

position = sys.stdin.readline() # a1
row = int(position[1]) # 행
column = int(ord(position[0])) - int(ord('a')) + 1
answer = 0

knight = [(-2, -1), (-2, 1), (-1, 2), (1, 2), 
          (2, 1), (2, -1), (1, -2), (-1, -2)]

for move in knight:
    nextRow = row + move[0]
    nextColumn = column + move[1]

    if 1 <= nextRow and nextRow <= 8 and 1 <= nextColumn and nextColumn <= 8:
        answer += 1

print(answer)