def solution(a, b):
    sum = 0

    if a == b:
        return a
    elif a < b:
        for i in range(a, b + 1):
            sum = sum + i
        return sum
    else:
        for i in range(b, a + 1):
            sum = sum + i
        return sum


# 다른사람의 풀이
def adder(a, b):
    # 함수를 완성하세요
    if a > b:
        a, b = b, a

    return sum(range(a, b+1))

#수열 n(n+1) // 2