data = []

for _ in range(9):
    temp = int(input())
    data.append(temp)

maxData = max(data)
for i in range(9):
    if data[i] == maxData:
        print(maxData)
        print(i + 1)
        break