def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6:
        pass
    else:
        return False

    for i in s:
        if i.isdigit():
            pass
        else:
            return False
    return True


# 다른사람 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)