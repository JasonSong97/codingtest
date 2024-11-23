def solution(my_string, is_suffix):
    answer = 0
    suffixLength = len(is_suffix)
    if is_suffix == my_string[len(my_string) - suffixLength: ]:
        return 1
    return 0