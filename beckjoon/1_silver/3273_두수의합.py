# 조합, for문은 실행시간 초과 -> 정렬을 통한 이분탐색 활용
import sys

number = int(input())
user_list = list(map(int, sys.stdin.readline().split()))
x = int(input())
left = 0
right = number - 1
cnt = 0

user_list.sort()

while left < right:
    tmp = user_list[left] + user_list[right]
    if tmp == x:
        cnt += 1
    if tmp < x:
        left += 1
    else:
        right -= 1

print(cnt)