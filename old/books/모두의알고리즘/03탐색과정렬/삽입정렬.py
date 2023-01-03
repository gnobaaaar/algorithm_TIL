def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        idx = i - 1
        while idx >= 0:
            if a[idx] < a[i]:
                a[idx], a[i] = a[i], a[idx] # 파이썬의 요소 바꾸는 함수
            else:
                idx -= 1
    return a

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)
