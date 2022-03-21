def solution(s):
    answer = ''
    lower_list = []
    upper_lsit = []

    for i in s:
        if i.islower():
            lower_list.append(i)
        else:
            upper_lsit.append(i)

    lower_list.sort(reverse=True)
    upper_lsit.sort(reverse=True)

    answer = ''.join(lower_list) + ''.join(upper_lsit)

    return answer


# 다른사람 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))