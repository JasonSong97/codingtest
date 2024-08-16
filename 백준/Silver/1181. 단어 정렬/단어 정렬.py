# 2초 2억번
# 길이가 짧은 것 먼저 앞으로 오고, 길이가 같은 경우 사전순서대로
# 단, 중복된 단어의 경우 1개는 삭제~

import sys

input = sys.stdin.readline

data = [input().rstrip() for _ in range(int(input()))]

setData = set(data) # 중복제거 후 새로운 변수에 담기

# 정렬기준에 바꿔서 바로 for 뤂핑
for d in sorted(setData, key=lambda x: (len(x), x)):
  print(d)
