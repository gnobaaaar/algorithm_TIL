num = int(input())
a = list(map(int, input().split()))

# print(min(a), end=" ")
# print(max(a))

min = a[0]
max = a[0]

for i in range(num):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]

print("{0} {1}".format(min, max))
