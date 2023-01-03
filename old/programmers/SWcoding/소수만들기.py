# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중
# 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록
# solution 함수를 완성해주세요.

# 입력값 [1,2,3,4] -> 1(개) -> 답 : 7
from itertools import combinations

def solution(nums):
    result = combinations(nums, 3)
    count = 0

    for r in result:
        num = r[0] + r[1] + r[2]
        check = 0
        for i in range(2, num):
            if num % i == 0:
                check = 1
        if check == 0:
            count += 1
    return count