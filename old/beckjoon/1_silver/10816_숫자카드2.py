# 내일 마저 도전
# upper bound lower bound 이해하기

# n = int(input())
# n_list = list(map(int, input().split()))
#
# m = int(input())
# m_list = list(map(int, input().split()))

n = 10
n_list = [6,3,2,10,10,10,-10,-10,7,3]
m = 8
m_list = [10,9,-5,2,3,4,5,-10]

def lower_case(list, target):
    # 끝자리 end값 때문에 -1을 제거한다
    start, end = 0, len(list)
    while start < end:
        mid = (start+end) //2
        if target > list[mid]:
            start = mid +1
        else:
            end = mid
    return end

def upper_case(list, target):
    start, end = 0, len(list)
    while start < end:
        mid = (start+end) //2
        if target >= list[mid]:
            start = mid +1
        else:
            end = mid
    return end

n_list.sort()
# print(n_list)

for i in m_list:
    print(upper_case(n_list, i)- lower_case(n_list, i), end=" ")
