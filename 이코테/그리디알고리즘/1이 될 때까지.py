n, k = map(int, input().split())
answer = 0

while True:
     if n == 1:
          break

     if n % k == 0:
          n = n / k;
     else:
          n -= 1
          
     answer += 1


print(answer)