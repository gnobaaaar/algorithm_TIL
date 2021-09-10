# a = int(input())
#
# for i in range(1, a):
#     for j in range((a-i)):
#         print(' ', end='')
#     for j in range((2*i)-1):
#         print('*', end='')
#     print()
#
# for i in range(a, 0, -1):
#     for j in range(a-i):
#         if i != a:
#             print(' ', end='')
#     for j in range((2*i)-1):
#         print('*', end='')
#     print()

n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    print()
for i in range(n, 0, -1):
    for j in range(n-i+1):
        print(' ', end='')
    for j in range(2*(i-1)-1):
        print('*', end='')
    print()