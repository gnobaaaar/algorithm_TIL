string = input().lower()
my_list = list(string)

# set 자료형을 통해 중복을 제거할 수 있다 -> 집합연산 가능
my_set = list(set(string))
cnt_list = []

for i in my_set:
    cnt = string.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    tmp = my_set[max_index]
    print(tmp.upper())