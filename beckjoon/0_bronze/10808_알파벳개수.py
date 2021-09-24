# alpha = ['a','b','c','d','e','f','g','h','i','j','k',
#          'l','m','n','o','p','q','r','s','t','u','v','w'
#          ,'x','y','z']
#
# user_input = list(map(str, input()))
#
# for i in alpha:
#     print(user_input.count(i), end=' ')

import sys

word = sys.stdin.readline().strip()
arr = [0 for _ in range(26)]

# 아스키코드를 활용하여 index 위치에 abc..순서로
for each in word:
    arr[ord(each)-97] += 1

print(" ".join(map(str, arr)))