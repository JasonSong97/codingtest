answer = []
for _ in range(int(input())):
  stk = []
  isVPS = True

  for c in input():
    if c == '(':
      stk.append(c)
    else:  # )
      if stk:
        stk.pop()
      else:
        isVPS = False

  if stk:
    isVPS = False

  answer.append(isVPS)

for a in answer:
  if a:
    print('YES')
  else:
    print('NO')
