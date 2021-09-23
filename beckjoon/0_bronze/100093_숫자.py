a_list = list(map(int, input().split()))

max_num = max(a_list)
min_num = min(a_list)
n = max_num-min_num-1

if max_num == min_num or min_num + 1 == max_num:
    n = 0
print(n)

for i in range(min_num+1, max_num):
    print(i, end=' ')