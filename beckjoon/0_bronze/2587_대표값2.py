a_list = []

for i in range(5):
    a_list.append(int(input()))

a_list.sort()
print(int(sum(a_list)/5))
print(a_list[2])