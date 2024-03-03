a = int(input())

result = 0
count = 0

while True:
     count += 1
     result += count
     if result >= a:
          break

print(result)