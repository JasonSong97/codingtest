def solution(price):
    if 500000 <= price:
        price *= 0.80
    
    elif 300000 <= price < 500000:
        price *= 0.90
        
    elif 100000 <= price:
        price *= 0.95
        
    return int(price)
