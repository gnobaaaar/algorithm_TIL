def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a
    pivot = a[-1]   # 마지막 값을 기준
    less =[]
    more =[]

    for i in range(0, n-1): # 마지막은 기준 값이므로 제외
        if a[i] < pivot:
            less.append(a[i])
        else:
            more.append(a[i])

    return quick_sort(less) + [pivot] + quick_sort(more)

d = [6,8,3,9,10,1,2,4,7,5]
print(quick_sort(d))