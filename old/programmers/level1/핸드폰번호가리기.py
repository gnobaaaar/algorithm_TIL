def solution(phone_number):
    answer = ''

    stringLength = len(phone_number) - 4
    firstString = stringLength * '*'
    answer = firstString + phone_number[stringLength:]

    return answer