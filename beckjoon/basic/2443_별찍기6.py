# a = int(input())

# for i in range(a):
#     for j in range(i):
#         if i > 0:
#             print(' ', end='')
#     for j in range((2* (a-i))-1):
#         print('*', end='')
#     print()

n=int(input())
for i in range(n):
    print(' '*i+'*'*(n-i)+'*'*(n-i-1))