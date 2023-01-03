a = int(input())
array = list(map(str, str(a)))

array.sort(reverse=True)
print("".join(array))

# 9부터 0까지 확인하면서 높은 순서로 출력을 해준다 -> O(n^2)
# array = input()
# for i in range(9, -1, -1):
#     for j in array:
#         if int(j) == i:
#             print(i, end='')