array_len = 9
max_num = 0
max_index = 0

for i in range(array_len):
    user_num = int(input())
    if max_num < user_num:
        max_num = user_num
        max_index = i

print(max_num)
print(max_index+1)