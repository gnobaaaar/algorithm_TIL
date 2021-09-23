a_list = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    b_list = a_list[a-1:b]
    b_list.reverse()
    a_list = a_list[:a-1] + b_list + a_list[b:]

for i in a_list:
    print(i, end=' ')
