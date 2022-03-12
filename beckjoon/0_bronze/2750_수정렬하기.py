array = []
for i in range(int(input())):
    array.append(int(input()))

array.sort()    # O(n log N)

for j in array:
    print(j)

# 선택 정렬 = 가장 작은 것을 찾아서 앞으로 보내어 정렬 O(n^2)
