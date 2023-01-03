def solution(s):
    tm = int(s)

    return tm

#다른사람풀이
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result

# 멋진 풀이입니다. 저도 완전 초보이지만 해설해 드리자면 str[::-1]은 주어진 스트링을 거꾸로 만들어 버립니다.
# 그 다음에 enumerate 함수를 이용하여 한 글자당 인덱스를 배정해서 각 자리에 10의 지수만큼 곱해서 더해주는 거네요.
# 예를 들면 "-1234"는 str[::-1]에 의해 "4321-"가 되고 4 * (10 ** 0) + 3 * (10 ** 1) + 2 * (10 **2) + 1 * (10 ** 3)를 한 이후에
# "-" 는 이 숫자를 마이너스로 만들어 버립니다.