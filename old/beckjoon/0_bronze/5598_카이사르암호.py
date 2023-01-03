a = input()
a_list = list(a)

for i in range(len(a_list)):
    if ord(a_list[i]) <= 67:
        # 문자열에서 ABC는 -3을 해도 원래 값이 아닌 xyz의 아스키값으로 이동
        print(chr(ord(a_list[i]) + 23), end='')
    else:
        print(chr(ord(a_list[i]) - 3), end='')