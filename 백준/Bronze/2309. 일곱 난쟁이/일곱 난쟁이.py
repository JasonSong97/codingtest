from itertools import combinations

people = [int(input()) for _ in range(9)]

answer = []
for i in combinations(people, 7):
  if sum(i) == 100:
    for data in sorted(i):
      print(data)
    break