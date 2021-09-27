# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         more = [i for i in array[1:] if i > pivot]
#
#         return quick_sort(less) + [pivot] + quick_sort(more)
#
# user_array = []
# for _ in range(int(input())):
#     user_array.append(int(input()))
#
# tmp = quick_sort(user_array)
#
# for i in tmp:
#     print(i)

array = []
for i in range(int(input())):
    array.append(int(input()))

array.sort()

for j in array:
    print(j)