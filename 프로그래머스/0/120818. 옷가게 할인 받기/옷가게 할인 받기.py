import math

def solution(price):
    if price >= 500000:
        return math.floor((price * 80) / 100)
    elif price >= 300000:
        return math.floor((price * 90) / 100)
    elif price >= 100000:
        return math.floor((price * 95) / 100)
    else:
        return price