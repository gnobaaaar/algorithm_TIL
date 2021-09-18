
list = []
for i in range(10):
    tmp = int(input())
    new_num = tmp % 42
    if new_num not in list:
        list.append(new_num)

print(len(list))