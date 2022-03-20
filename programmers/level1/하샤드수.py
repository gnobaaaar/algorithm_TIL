def solution(x):
    answer = True

    numList = list(map(int, str(x)))
    sum = 0

    for i in numList:
        sum = sum + i

    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer


# better
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0
