d = dict()

for _ in range(int(input())):
  book = input()
  if book in d:
    d[book] += 1
  else:
    d[book] = 1

answer = []

maxValue = max(d.values())
for k, v in d.items():
    if v == maxValue:
        answer.append(k)

answer.sort()
print(answer[0])
