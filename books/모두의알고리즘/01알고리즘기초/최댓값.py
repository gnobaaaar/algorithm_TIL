# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값
#1번을 해보세요!
def find_max(a):
    n = len(a)
    max = a[0]
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
    return max

v = [17, 92, 18, 33, 58, 7, 33, 42]
#2번을 해보세요!
print(find_max(v))