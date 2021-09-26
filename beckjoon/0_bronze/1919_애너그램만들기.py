a = list(input())
b = list(input())
cnt = 0
index = 0

while index < len(a):
    if a[index] in b:
        b.pop(b.index(a[index]))
        a.pop(index)
        cnt += 2
    else:
        index += 1

print(len(a)+len(b))