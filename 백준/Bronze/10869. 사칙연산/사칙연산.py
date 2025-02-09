import sys

input = sys.stdin.readline

a, b = map(int, input().split())
# A+B, A-B, A*B, A/B(몫), A%B(나머지)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)