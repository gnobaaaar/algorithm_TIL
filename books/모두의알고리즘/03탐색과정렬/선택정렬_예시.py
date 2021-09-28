# 쉽게 설명한 선택 정렬
# 입력: 리스트 a
# 출력: 정렬된 새 리스트

# 주어진 리스트에서 최솟값의 위치를 돌려주는 함수

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx
# 1번을 해보세요!
def sel_sort(a):
    result = []
    while a:
        min = find_min_idx(a)
        value = a.pop(min)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))
