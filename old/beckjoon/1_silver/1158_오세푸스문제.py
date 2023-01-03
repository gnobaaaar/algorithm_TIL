a, b = map(int, input().split())
index = 0
a_list = []
b_list = []

for i in range(1, a+1):
    a_list.append(i)

# for j in range(a):
#     index += b-1
#     if index >= len(a_list):
#         index = index % len(a_list)
#     b_list.append(str(a_list.pop(index)))

while a_list:
    index = (index + (b-1)) % (len(a_list))
    b_list.append(str(a_list.pop(index)))

print("<", ", ".join(b_list), ">", sep='')