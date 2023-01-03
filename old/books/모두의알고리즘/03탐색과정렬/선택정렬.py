# 선택 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)
# 1번을 해보세요!

def sel_sort(a):
    for i in range(0, len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
