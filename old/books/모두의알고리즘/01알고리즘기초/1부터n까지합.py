# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
# 입력: n
# 출력: 1부터 n까지의 숫자를 더한 값
# 1번을 해보세요!

def sum_n(num):
    s = 0
    for i in range(1, num+1):
        s += i
    return s

#2번을 해보세요!
print(sum_n(10))

#3번을 해보세요!
print(sum_n(100))