n = int(input())
a = list(map(int, input().split()))
test = a[0]

for i in range(1, n):
    if test > a[i]: 
        test = a[i]

print(test)