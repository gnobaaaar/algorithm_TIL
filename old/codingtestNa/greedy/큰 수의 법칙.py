# 입력 부분 해결
user_input = list(map(int, input().split()))
array_input = list(map(int, input().split()))
array_input.sort(reverse=True)

# 구현
bigNum = array_input[0]
nextNum = array_input[1]

tmp = user_input[2]
sum = 0
for i in range(user_input[1]):
    if tmp > 0:
        sum += bigNum
        tmp -= 1
    else:
        sum += nextNum
        tmp = user_input[2]

print(sum)
