def binary_search_sub(a, x, start, end):
    # 종료 조건: 남은 탐색 범위가 비었으면 종료

    if start > end:
        return -1

    mid = (start + end) // 2  # 탐색 범위의 중간 위치

    if x == a[mid]:  # 발견!

        return mid

    elif x > a[mid]:  # 찾는 값이 더 크면 중간을 기준으로 오른쪽 값을 대상으로 재귀 호출

        return binary_search_sub(a, x, mid + 1, end)

    else:  # 찾는 값이 더 작으면 중간을 기준으로 왼쪽 값을 대상으로 재귀 호출

        return binary_search_sub(a, x, start, mid - 1)

    return -1  # 찾지 못했을 때


# 리스트 전체(0 ~ len(a) - 1)를 대상으로 재귀 호출 함수 호출

def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a) - 1)


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))