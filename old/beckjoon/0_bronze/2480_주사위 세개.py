user_input = list(map(int, input().split()))
user_set = set(user_input)
max_num = 0
a_list = []


if len(user_set) == 1:
    print(10000 + user_input[0] * 1000)
elif len(user_set) == 3:
    print(max(user_input) * 100)
else:
    for i in user_set:
        if user_input.count(i) == 2:
            max_num = i
    print(1000 + max_num * 100)


