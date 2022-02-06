# num = int(input())
# lists = list(map(int, input().split()))
# min = lists[0]
# max = lists[0]
#
# for i in range(num):
#     if lists[i] < min:
#         min = lists[i]
#     if lists[i]  > max:
#         max = lists[i]
# print(min, max)

num = int(input())
lists = list(map(int, input().split()))

for i in range(num):
    if lists[i] > lists[i+1]: