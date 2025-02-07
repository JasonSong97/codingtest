def solution(a, b):
    one = int(str(a) + str(b))
    two = 2 * a * b
    if one == two:
        return one
    elif one > two:
        return one
    else:
        return two
