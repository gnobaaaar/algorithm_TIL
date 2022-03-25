def solution(s):
    answer = True
    p_count = 0
    y_count = 0

    for i in s:
        if i == 'p' or i == 'P':
            p_count += 1
        elif i == 'y' or i == 'Y':
            y_count += 1

    if p_count == y_count:
        return True
    else:
        return False

    return True


# 다른 사람의 풀이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')