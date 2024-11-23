def solution(my_string, is_prefix):
    answer = 0
    prefixLength = len(is_prefix)
    if is_prefix == my_string[: prefixLength]:
        return 1
    return 0