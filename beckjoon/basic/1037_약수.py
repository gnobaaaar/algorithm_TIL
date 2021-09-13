user_num = int(input())
user_input = list(map(int, input().split()))
user_input.sort(reverse=True)

print(user_input[0] * user_input[-1])

# max = max(user_input)
# min = min(user_input)
