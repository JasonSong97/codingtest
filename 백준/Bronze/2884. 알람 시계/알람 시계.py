import sys
input = sys.stdin.readline

hour, minute = map(int, input().split())
# 10 10 => 610 - 45 = 565 => 9 25
# 0 30 =>  30 - 45 => -15 => 

finalMinute = 60 * hour + minute - 45
if finalMinute >= 0:
    print(finalMinute // 60, end = " ")
    print(finalMinute % 60)
else:
    print(23, end = " ")
    print(finalMinute + 60)
