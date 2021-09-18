a = int(input())
check = a
new_num = 0
tmp = 100
i = 0

while True:
    tmp = (a // 10) + (a % 10)
    new_num = (a%10)*10 + (tmp%10)
    a = new_num
    # print("현재숫자", tmp)
    i += 1
    if check == a:
        break
print(i)