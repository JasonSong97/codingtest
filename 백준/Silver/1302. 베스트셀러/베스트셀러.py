m = {}
for _ in range(int(input())):
  word = input()
  if word not in m:
    m[word] = 1
  else:
    m[word] += 1

answer = []
for k, v in m.items():
  if v == max(m.values()):
    answer.append(k)

answer.sort()
print(answer[0])
