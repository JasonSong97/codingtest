a, b = input().split()  # 사용자로부터 정수를 입력받음
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))