# 최댓값의 위치 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중에서 최댓값이 있는 위치(0부터 n-1까지의 값)
#1번을 해보세요!
def find_max_idx(a):
    max_idx = 0
    for i in range(1, len(a)):
        if a[max_idx] < a[i]:
            max_idx = i
    return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
#2번을 해보세요!
print(find_max_idx(v))
