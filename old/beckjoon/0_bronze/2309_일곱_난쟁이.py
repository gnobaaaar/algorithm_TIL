from itertools import combinations

# a_list = [20, 7, 23, 19, 10, 15, 25, 8, 13]
a_list = []
b_list = [0] * 9
c_list = []

for i in range(9):
    a_list.append(int(input()))

a_list.sort()
b_list = list(combinations(a_list, 7))

for i in b_list:
    if sum(i) == 100:
        c_list = i

for i in c_list:
    print(i)