def d(n):
    next = n
    # 숫자를 자릿수별로 리스트화 만들기 -> 파이썬 활용
    for i in list(str(n)):
        next += int(i)
    return next

array = []

for i in range(10001):
    array.append(d(i))

# array.sort()

for j in range(1, 10000):
    if j in array:
        continue
    else:
        print(j)